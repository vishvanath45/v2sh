from pymongo import MongoClient
client = MongoClient('35.187.229.248')

#Uncomment the environement you are working on !!!

# Development Settings 
# DO NOT CHANGE !! 
client.db_dev.authenticate('codes_for_living','kaise_kiya_bhaiya?',mechanism='SCRAM-SHA-1')
db = client['db_dev']
experience = db['Experience']
superuser = db['SuperUser']
user = db['User']
credentials = db['credentials']
session = db['Session_table']
# Production Settings 
# DO NOT CHANGE !! 
# client.db_prod.authenticate('root_su','yeh_production_db_h',mechanism='SCRAM-SHA-1')
# db = client['db_prod']
# experience = db['Experience']
# superuser = db['SuperUser']
# user = db['User']
#credentials = db['credentials']

# Backup Settings 
# DO NOT CHANGE !! 
# client.db_backup.authenticate('last_hope','agar_yeh_gaya_toh_sab_gaya0xx0',mechanism='SCRAM-SHA-1')
# db = client['db_prod']
# experience = db['Experience']
# superuser = db['SuperUser']
# user = db['User']'
#credentials = db['credentials']