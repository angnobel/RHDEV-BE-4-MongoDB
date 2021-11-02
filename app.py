# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password
from db import db
URL = "URL_LINK".format(
    DB_USERNAME, DB_PWD)
print(URL)
client = pymongo.MongoClient(URL)
db = client["RHDEVS-BE-Mongo"]

# Create

# Read

# Update

# Delete
