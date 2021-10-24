from db import *
import pymongo
import datetime

URL = DB_LINK.format(
    DB_USERNAME, DB_PWD)

client = pymongo.MongoClient(URL)
db = client["RHDEVS-BE-Mongo"]


neworder = {"orderID": 11, "amount": 1, "userID": 2, "shopID" : 4, "status" : "Ordered", "orderDate":datetime.datetime.now()}
db.Orders.insert_one(neworder)

cursor = db.Orders.find().sort("amount",1)
print(list(cursor[5:10]))

specificdate = datetime.datetime(2021,10,22,0,0,0)
conditiontofilter = {"$and" : [ {"status": {"$in": ["Failed", "Completed"] } }, {"orderDate": {"$gt":specificdate} }]}

results = db.Orders.update_many(conditiontofilter, {"$set": {"status" :"dispute"}})
print(results.modified_count)

delresults = db.Orders.delete_one({"orderID":3})
print(delresults.deleted_count)