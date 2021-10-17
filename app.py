# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import DB_PASSWORD, DB_USER, URL_LINK
import pymongo
import datetime

URL = URL_LINK.format(DB_USER, DB_PASSWORD)
client = pymongo.MongoClient(URL)
db = client["RHDEVS-BE-Mongo"]

# Create

###
# creating object to insert into Orders table
###

shop = db.shops.find_one({"shopName": "Kimly Dim Sum"})
user = db.users.find_one({"name" : "Charles Lim"})

data = {}
data["customer"] = {"userID" : user["_id"], "name": user["name"], "address": user["address"]}
data["shop"] = {"shopID" : shop["_id"], "shopName": shop["shopName"]}
data["amount"] = 42.90
data["status"] = 'In Progress'
data["orderDate"] = datetime.datetime.utcnow()

# result1 = db.orders.insert_one(data)
# print(result1.inserted_id)

# Read

###
# Retrieve the 5th-10th largest transactions
###

cursor1 = db.orders.find().sort("amount", pymongo.DESCENDING).skip(4).limit(6)
# for i in list(cursor1):
#     print(i)
    
# Update

###
# Update orders with status (Complete/Failed) and orderDate (after a specific date), update status to (Dispute)
###



# Delete

###
# Delete all orders with a specific orderID
###

