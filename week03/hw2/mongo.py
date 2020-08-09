import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
mydb = client['lagou']
mycollection = mydb['collection_lagou']