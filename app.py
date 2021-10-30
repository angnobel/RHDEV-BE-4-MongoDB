# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import URL
import pymongo
from pymongo import MongoClient
import datetime

cluster = MongoClient(URL)
db = cluster["RHDEVS-BE-Mongo"]

# Create
db.Order.insert_one({"userid":"6173caf0e8e55381ed3f94c5", 
                    "shopid" : "6173bfb4e8e55381ed3f94ac", 
                    "amount": 9, 
                    "status":"Processing", 
                    "orderDate": datetime.datetime.now()})

# Read
fifthToTenthLargest = db.Order.find().sort('amount', -1)[4:9]

# Update
someDate = datetime.datetime(2020,10,25)
condition = {"$and": [{"status": {"$in": ["Failed", "Completed"] }}, {"orderDate": {"$gt" :someDate}} ] }
updateResult = db.Order.update_many(condition, {"$set": {"status": "Dispute"}})

# Delete
db.Order.delete_many({"orderID":"1111111111111"})