from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

db = conn.mydb

collection = db.student

collection.update({"name":"Jack"},{"$set":{"age":25}})

conn.close()