import predictionio
import MySQLdb
from datetime import datetime
import argparse
import pytz
import sys
import json
from pprint import pprint

def export_events(client):
	print client.get_status()
	print "Exporting data..."
	engine_client = predictionio.EngineClient(url="http://52.8.31.209:8888")
	data=engine_client.send_query({"user": "1", "num": 4})
	#pprint(data)
	value_score=[]
	value_item=[]
	incr=0
#strvalue=json.dumps(data,separators=(',',':'))
#print strvalue
	myDbConn = MySQLdb.Connect(host = '127.0.0.1',
                         user = 'root',
                         passwd = 'nathiya',
                         db = 'predictionio')
	cur = myDbConn.cursor()
 
	for key in data.keys():
		strvalue = (data[key])
		print strvalue
	for i in range(len(strvalue)):
		print strvalue[i]
		for k in strvalue[i].keys():
			item=strvalue[k]
			score=strvalue[k+1]
			print item,score
		'''	if (k=='item'):
				value_item.append(v)
				
			else:
				value_score.append(v)
	print value_item,value_score'''
'''	for i in value_item:
		item=i
		print item
		for j in value_score:
			score=j
			user_id=1
			print score
			add_event=('INSERT INTO eventdata(user_id,recom_item_id,score)VALUES(%s,%s,%s)')
			add_event=("INSERT INTO event_data(user_id,Recom_item_id,score)VALUES(%s,%s,%d)")
			data_event=(1,item,score)
			cur.execute(add_event,(user_id,item,score))
	cur.execute(sql,("192.168.1.84",json.dumps(dict)))
	myDbConn.commit()'''
	#myDbConn.close()
	#print "Done"
if __name__ == '__main__':
	parser = argparse.ArgumentParser(
    description="Import data for e-commerce recommendation engine")
	parser.add_argument('--access_key', default='91TM7HTHJvW0jb6kR8c8bkUe3BFZAu4N3vAI6wIuzc84zqpoHs6NlUe737ijKK0S')
	parser.add_argument('--url', default="http://52.8.31.209:7070")

	args = parser.parse_args()
	print args
	client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
	export_events(client)
