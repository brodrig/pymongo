from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.zipcodes
collection = db.zips

docs = collection.find(
    {"city" : {"$in" : ["BUFFALO", "NEW YORK"]}},  # query
    {"city" : 1,  "state" : 1, "_id" : 1, "pop" : 1}  # projection
)  # cursor object

# docs = collection.find({})

for i, document in enumerate(docs):
    print "{}: {}".format(i, document)
