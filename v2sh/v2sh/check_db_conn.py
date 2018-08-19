'''
This is just a individual script to check DB connection 
May be useful for debugging purposes.
'''

from pymongo import MongoClient
import pprint

client = MongoClient('35.187.229.248')
# If true, connection successful

# Read only
client.db_prod.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')

db = client[DB_NAME]

collection = db[COLLECTION_NAME]

print(collection)

k = collection.insert({'name':'shasdaxxxrma'})
