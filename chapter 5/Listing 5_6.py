#Listing 5_6: MongoClient
from pymongo import MongoClient
client = MongoClient()
db=client.newdb
col=db['books']
