from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

db = conn.mydb

collection = db.student

collection.remove({"name":"Jack"})

conn.close()