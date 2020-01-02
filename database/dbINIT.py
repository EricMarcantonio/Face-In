'''
Create and make schema for images. Store images as base64 strings and then convert them
'''

from pymongo import MongoClient

client = MongoClient()
peopleDB = client["people"]
nameCollection = peopleDB["names"]


