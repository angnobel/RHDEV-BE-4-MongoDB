import pymongo
import datetime
from db import db

# Create
order__id = db.Orders.insert_one({"OrderID": "A12", "amount": 1.6, "userID":1, "shopID":1, "status":"preparing"})




# Read 5th to 10th largest transactions
cursor = db.Orders.find().sort("amount", -1)
cursor = list(cursor[4:9])
print(cursor)


# update all orders with status (Failed OR Completed) AND after a date(bad_date in this case)
bad_date = datetime.datetime(2021 , 8 , 26 , 20 , 6 , 31) 
filter_con = { "OrderDate" : {"$gte" : bad_date} , "$or":[{"status" :"Failed"}, {"status" :"Completed"}] } 
new_con = { "$set" : { 'status': "Dispute" } }
# db.Orders.update_many(filter_con, new_con)

# Delete all orderUpdates with a orderID
# db.Orders.delete_many({ "OrderID" : {"$exists": True } })

