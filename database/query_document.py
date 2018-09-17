import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId  # used to id query

conn = MongoClient("localhost", 27017)

db = conn.mydb

collection = db.student

res = collection.find({"age": {"$gt": 18}})
print(res.count())
for row in res:
    print(row)
    print(type(row))

'''
return all record
res=collection.find() 
for row in res:
    print(row)
    print(type(row))
'''
res1 = collection.find({"_id": ObjectId("1131312212b019addd14")})
print(res1[0])

# res2=collection.find().sorted("age") #asc order
res2 = collection.find().sorted("age", pymongo.DESCENDING)  # desc order
for row in res2:
    print(row)

res3 = collection.find().skip(3).limit(3)
for row in res2:
    print(row)

conn.close()
