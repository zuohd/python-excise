from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

db = conn.study

collection = db.student

collection.remove({"name":"Jack"})

conn.close()