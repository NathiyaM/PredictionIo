import predictionio 
import MySQLdb 
client = predictionio.EventClient( 
access_key = "91TM7HTHJvW0jb6kR8c8bkUe3BFZAu4N3vAI6wIuzc84zqpoHs6NlUe737ijKK0S", 
url = "http://52.8.31.209:7070" 
) 
 
print client.get_status() 
client.close() 
