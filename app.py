# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import db
import pymongo
import json
import datetime

# Create
returnResult =  db.Orders.insert_one({"orderID":5,"amount":2,"userID":190,"shopID":2290,"status":"pending","date":2021-10-12})
print(returnResult.inserted_id)

# Read
cursor = db.Orders.find().sort("amount",pymongo.DESCENDING).skip(4).limit(6)
list(cursor)

# Update
dateLimit = datetime.datetime(2021,10,5,0,0,0)
filter_con = {"$and":[{"status":["Completed","Failed"]},{"date":{"$gt":dateLimit}}]}
new_con = {"$set":{"status":"Dispute"}}
updateResult = db.Orders.update_many(filter_con,new_con)
print(updateResult.modified_count)

# Delete
del_orderID = {"$oid":"6161cbd633768c80aebdcf28"}
deleteResult = db.Orders.delete_one({"orderID":del_orderID})
print(deleteResult.deleted_count)