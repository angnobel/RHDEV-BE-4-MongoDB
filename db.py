import pymongo
from datetime import date, datetime

dbUsername = ""
dbPassword = ""

###############################################################
#           db.py key: Lesson Learnt -- Do not share          #
###############################################################
URL = "mongodb+srv://" + dbUsername + ":" + dbPassword + \
    "@mycluster.vv19r.mongodb.net/FoodOrderDemo?retryWrites=true&w=majority"
client = pymongo.MongoClient(URL)
db = client["FoodOrderDemo"]

################################################
#                   Question 1                 #
################################################


def questionOne(orderID, userID, shopID, amount):
    try:
        db.Orders.insert_one({
            "orderDate": datetime.today(),
            "orderID": orderID,
            "userID": userID,
            "amount": amount,
            "shopID": shopID,
            "status": "processing order"
        })
        return "Sucessfully Ordered"

    except Exception:
        return "Error in Ordering"

################################################
#                   Question 2                 #
################################################


def questionTwo():
    try:
        stageOne = {"$sort": {"amount": -1}}
        pipeline = [stageOne]
        array = list(db.Orders.aggregate(pipeline))
        if len(array) < 10:
            return "Error. Less than 10 orders"
        else:
            while len(array) > 5:
                array.pop()
            return array

    except Exception:
        return "Error in retrieving data"

################################################
#                   Question 3                 #
################################################


def questionThree(invalid_date):
    try:
        filter_con1 = {"$or": [{"status": "Failed"}, {"status": "Completed"}]}
        filter_con2 = {"orderDate": {"gte": invalid_date}}
        combined_filter = {"$and": [filter_con1, filter_con2]}
        update_con = {"$set": {"status": "Dispute"}}
        db.Orders.update(combined_filter, update_con)
        return "Status Updated"

    except Exception:
        return "Invalid Request"

################################################
#                   Question 4                 #
################################################


def questionFour(orderID):
    try:
        db.Orders.delete_many({"orderID": orderID})
        return "successfully deleted"

    except Exception:
        return "Invalid Request"
