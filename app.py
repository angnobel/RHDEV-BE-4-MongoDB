# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import DB_USERNAME, DB_PWD, URL_LINK
import pymongo
import datetime
URL = URL_LINK.format(
    DB_USERNAME, DB_PWD)
print(URL)
client = pymongo.MongoClient(URL)
db = client["RHDEVS-BE-Mongo"]
# Create

order={
    "orderID": 11,
    "amount": 23,
    "shop": {
        "shopID": 3,
        "shopName": "Noodles",
    },
    "status": "Completed",
    "orderDate": datetime.datetime.now()
}
db.orders.insert_one(order)
db.users.update_one({"username":"justin"}, 
                {
                    '$push': {
                        "orders": 11
                    }
                }
                )

# Read
orders_sorted = db.orders.find().sort("amount", pymongo.ASCENDING).skip(4).limit(6)


# Update
statusUpdate = db.orders.update_many(
    {"orderDate" : { '$gt' : datetime.datetime(2021, 10, 27, 0, 0, 0) }},
    {"$set": {"status": "Dispute"}},
)
print(statusUpdate.modified_count)

# Delete
deleteUpdate = db.orders.delete_many(
    {"orderID": {"$eq": 11}}
)
print(deleteUpdate.deleted_count)