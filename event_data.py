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
	user_id=raw_input("enter the customer_id")
	num=int(raw_input("Enter the number of recommendations"))
	engine_client = predictionio.EngineClient(url="http://52.8.31.209:8888")
	data=engine_client.send_query({"user": user_id, "num": num})
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
		for k,v in strvalue[i].items():
			print k,v
			if (k=='item'):
				event_item=v
				
			else:
				event_score=v
		user_id=1	
		add_event=('INSERT INTO eventdata(user_id,recom_item_id,score)VALUES(%s,%s,%s)')
		cur.execute(add_event,(user_id,event_item,event_score))
	myDbConn.commit()
	myDbConn.close()
	print "Done"
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
