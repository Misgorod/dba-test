import time
import pymongo

while True:
    try:
        client = pymongo.MongoClient('mongodb://mongo:27017/')
        response = client.test.command('ping')
        print(f"response: {response}")
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
    
    