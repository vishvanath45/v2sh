from pymongo import MongoClient
client = MongoClient(IP)

client.db_prod.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')
db = client['db_prod']
experience = db['Experience']
superuser = db['SuperUser']
user = db['User']
credentials = db['credentials']
session = db['Session_table']
