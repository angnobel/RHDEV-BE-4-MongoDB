import pymongo
from db import db

# Create
order__id = db.Orders.insert_one({"OrderID": "A12", "amount": 1.6, "userID":1, "shopID":1, "status":"preparing"})
print(order__id)

# Read 5th to 10th largest transactions
cursor = db.Orders.find().sort("amount", -1)
cursor = list(cursor[4:9])
print(cursor)
# Update


# Delete
