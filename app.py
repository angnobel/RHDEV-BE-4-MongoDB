from db import db
import pymongo
from datetime import date, datetime

###################################
#              CREATE             #
###################################

def createOrder(orderID, amount, userID, shopID):
    try:
        db.Orders.insert_one({
            "orderDate": datetime.today(),
            "orderID": orderID,
            "userID": userID,
            "amount": amount,
            "shopID": shopID,
            "status": "processing order"
            })

        return "Order Successfully Created"

    except Exception:
        return "Invalid Request"

##########################################
# Delete all orderUpdates with a orderID #
##########################################


def orderUpdates(orderID):
    try:
        db.Orders.delete_many({"orderID": orderID})
        return "successfully deleted"

    except Exception:
        return "Invalid Request"

##################################################################
# For all orderUpdates created with status (Failed OR Completed) #
#         AND after a date, update the status to Dispute         #
##################################################################

def updateStatus(invalid_date):
    try:
        filter_con1 = {"$or": [{"status": "Failed"}, {"status": "Completed"}]}
        filter_con2 = {"orderDate": {"gte": invalid_date}}
        combined_filter = {"$and": [filter_con1, filter_con2]}
        update_con = {"$set": {"status": "Dispute"}}
        db.Orders.update(combined_filter, update_con)
        return "Status Updated"

    except Exception:
        return "Invalid Request"

###############################################
# Retrieve the 5th -10th largest transactions #
###############################################
def filterCondition():
    try:
        cursor = db.Orders.find()
        return list(cursor.sort("amount", pymongo.ASCENDING).skip(4))

    except Exception:
        return "Invalid Request"
