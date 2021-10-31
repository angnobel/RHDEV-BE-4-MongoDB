# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
import datetime
import db
import pymongo
db = db.rhdevsdb

date = datetime.datetime.now()
formatted_date = date.strftime("%x") + " " + date.strftime("%X")

# Create
returnResult = db.Orders.insert_one({
    "orderID":"113",
    "amount":"399" ,
    "userID":"30",
    "shopID":"13",
    "status":"Completed",
    "orderDate" : formatted_date
})

# Read
cursor = db.Orders.find({})
sort = ("amount", pymongo.DESCENDING)
print(list(cursor)[5:11])

# Update
condition = datetime.datetime(2021,6,5,0,0,0)
conditional_date = condition.strftime("%x") + " " + condition.strftime("%X")
filter_con1 = { "status" : {"$in": ["Completed", "Failed"]} }
filter_con2 = { "orderDate" : {"$gte" : conditional_date}}
db.Orders.update_many({"$and" : [filter_con1, filter_con2]}, {"$set" : {"status": "Dispute"}})


# Delete
db.Orders.delete_one({"orderID": "101"})
