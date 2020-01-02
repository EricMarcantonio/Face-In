from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client['people']
#
# article = {"author": "Derrick Mwiti",
#            "about": "Introduction to MongoDB and Python",
#            "tags":
#                ["mongodb", "python", "pymongo"]}
#
#
# people = db['people']
#
# result = people.insert_one(article)

for bet in db["people"].find():
    print (bet)


