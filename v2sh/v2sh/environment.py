from pymongo import MongoClient
client = MongoClient(IP)

#Uncomment the environement you are working on !!!

# Development Settings
# DO NOT CHANGE !!
# client.db_dev.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')
# db = client['db_dev']
# experience = db['Experience']
# superuser = db['SuperUser']
# user = db['User']
# credentials = db['credentials']
# session = db['Session_table']

# Production Settings
# DO NOT CHANGE !!
client.db_prod.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')
db = client['db_prod']
experience = db['Experience']
superuser = db['SuperUser']
user = db['User']
credentials = db['credentials']
session = db['Session_table']

# Backup Settings
# DO NOT CHANGE !!
# client.db_backup.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')
# db = client['db_prod']
# experience = db['Experience']
# superuser = db['SuperUser']
# user = db['User']'
#credentials = db['credentials']
