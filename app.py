# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import db
from db import DB_PASSWORD, DB_USERNAME, URL_LINK
import pymongo
from bson.objectid import ObjectId
import datetime

URL = URL_LINK.format(DB_USERNAME, DB_PASSWORD)
client = pymongo.MongoClient(URL)
db = client["RHDEVS-BE-Mongo"]

# Create

shop = db.shop.find_one({"shopName": "Al Amaans"})
user = db.users.find_one({"userID": 1})

order = {}
order["customer"] = {"userID": user["userID"], "name": user["name"], "address": user["address"]}
order["shop"] = {"shopID": shop["shopID"], "shopName": shop["shopName"]}
order["amount"] = 10.00
order["status"] = "order successful"
order["orderDate"] = datetime.datetime.utcnow()

# returnedResult1 = db.orders.insert_one(order)
# print(returnedResult1.inserted_id)

# Read

cursor = db.orders.find().sort("amounts", pymongo.DESCENDING)

print(cursor[4:9])

# Update

targetDate = datetime.datetime(2021,12,31,0,0,0,0)
filter_condition = {"$and": [ 
        {"status": {"$in": ["Completed", "Failed"]}},
        # {"$or": [{"status": "Completed"},{"status": "Failed"}]}
        {"orderDate": {"$gt": targetDate}}]
    }

returnedResult2 = db.orders.update_many(filter_condition, {"$set": {"status": "Dispute"}})

print(returnedResult2.modified_count)



# Delete

orderID = 54321
returnedResult3 = db.orders.delete_one({"orderID": orderID})
print(returnedResult3.deleted_count)