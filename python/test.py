from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017/')
response = client.test.command('ping')
print(response)