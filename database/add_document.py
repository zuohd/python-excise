# pip install pymongo

from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

db = conn.mydb

collection = db.student

collection.insert({"name":"Jack","age":18,"gender":1,"address":"上海","isDeleted":0})


conn.close()