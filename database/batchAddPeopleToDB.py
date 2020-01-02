import base64
from os import listdir

from pymongo import MongoClient

client = MongoClient()
peopleCollection = client["people"]["users"]
registeredCollection = client["people"]["registered"]


def addFromFolder(parentDirectory):
    for subdirNamePerson in listdir(parentDirectory):
        name = subdirNamePerson
        imageList = []

        for eachPhoto in listdir(parentDirectory + "/" + subdirNamePerson):
            with open(parentDirectory + "/" + subdirNamePerson + "/" + eachPhoto, "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
                imageList.append(str)
        if (peopleCollection.find(name))
        result = peopleCollection.insert_one({
            "name": name,
            "photoArray": imageList
        })

        print(result.acknowledged)

        result = registeredCollection.insert_one({
            "name": name,
            "reg": False
        })
        print(result.acknowledged)


addFromFolder('../rawPictures')

for i in peopleCollection.find():
    peopleCollection.delete_many(i)

for x in  registeredCollection.find():
    registeredCollection.delete_many(x)