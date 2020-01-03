import pymongo
from bson import objectid, json_util
import json

# Connection String
class Mongodb(object):
    # INIT FUNCTION
    def __init__(self, connectionString, db):
        print("Attempting to Connect with database")
        try:
            self.connection = pymongo.MongoClient(connectionString) # initiating connection with database
            self.db = self.connection[db]
            print("Connected with database")
        except Exception as e:
            print(e)

    # APPENDs Document to collection
    def Append(self, collection, params):
        try:

            _id = self.db[collection].insert_one(params)
            print("ID: %s"%(objectid.ObjectId(_id.inserted_id)))
            return {
                "response": True,
                "_id": str(objectid.ObjectId(_id.inserted_id))
            }

        except Exception as e:
            print(e)
            return False

    # UPDATEs Documents in collection
    def Update(self, collection, id, params):
        try:
            self.db[collection].find_one_and_update({"_id", objectid.ObjectId(id)}, params)
            print("database updated")
            return True
        except Exception as e:
            print(e)
            return False

    # LOGs all information
    def Log(self, path, method, params, time):
        try:
            self.db["Logs"].insert_one({"path": path, "method": method, "params": params, "time": time })
            print("Request Logged")
        except Exception as e:
            print(e)
    
    def ReadSingle(self, docID):
        data = self.db["Users"].find({"_id": objectid.ObjectId(docID)}, {"_id":1, "name":1, "RegisterationStatus":1, "images":1})
        x = data.next()
        x["_id"] = str(objectid.ObjectId(x["_id"]))
        return {
            "response": True,
            "data": x
        }

    def ReadAll(self):
        # docs = []
        docs = json_util.dumps(self.db["Users"].find())
        # x = data.next()
        # x["_id"] = str(objectid.ObjectId(x["_id"]))
        # for i in data.where():
        #     x = data.next()
        #     x["_id"] = str(objectid.ObjectId(x["_id"]))
        #     docs.append(x)

        return {
            "response": True,
            "data": docs
        }