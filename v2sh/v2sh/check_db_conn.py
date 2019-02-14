'''
This is just a individual script to check DB connection
May be useful for debugging purposes.
'''

from pymongo import MongoClient
import pprint

client = MongoClient(IP_ADDR)
# If true, connection successful
print(client)
# Read only
client.db_prod.authenticate(USERNAME,PASSWORD,mechanism='SCRAM-SHA-1')

db = client[DATABASE]

collection = db[collection]

print(collection)

k = collection.insert({'name':'shasdaxxxrma'})
