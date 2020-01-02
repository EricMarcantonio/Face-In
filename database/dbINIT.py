'''
Create and make schema for images. Store images as base64 strings and then convert them
'''

from pymongo import MongoClient

client = MongoClient()


peopleDB = client["people"]
names = peopleDB["names"]

for i in names.find():
    result = names.delete_many(i)
    print(result.deleted_count)
