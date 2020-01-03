import base64 # for base64 decoding 
from flask import Flask, render_template, request, jsonify # flask related 
from db import Mongodb
from datetime import datetime

app = Flask(__name__)

# Initating connection with mongodb
dbClient = Mongodb("mongodb://localhost:27017/", "Personal")

# DEFAULT ROUTE
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# RECIEVES IMAGE AS POST
# {
    # image: "base-64-encoded-image-data"
# }
@app.route("/valuation", methods=["POST"])
def getImage():
    if (request.method == "POST"): # checking if request is post
        image = request.get_json(force=True)["image"]
        image = image[image.index(",")+1:] # removing descriptor for the data data:image/png;base64,
        dbClient.Log("/valuation", "POST", {"image": image}, datetime.now()) # api request logs        
        params = {
            "path": "/valuation",
            "method": "POST",
            "image": [image],
            "time": datetime.now()
        }
        dbClient.Append("Testing", params) # api requests for valuation
        return "YES or NO depending on model response" # depending on the response return a response 
    else:
        return "Invalid Request Method"


@app.route("/admin/home", methods=["GET"])
def adminHome():
    return "RETURN ADMIN HOME"


# Batch Upload user photos
@app.route("/admin/user/add", methods=["POST"])
def adminUpload():
    if (request.method == "POST"):
        name = request.get_json(force=True)["name"] # getting users name
        images = request.get_json(force=True)["images"] # getting array of images associated with the user
        registeration_status = request.get_json(force=True)["RegisterationStatus"]
        
        # removing image descriptors
        # for i in range(len(images)):
        #     images[i] = images[i][images[i].index(",")+1:] # removing descriptor for the data data:image/png;base64,

        # User information
        params = {
            "name": name,
            "images": images,
            "RegisterationStatus": registeration_status
        }
        # saving users information to collection
        repsonse = dbClient.Append("Users", params) # returns True/False depending on if the user document was created

        # api request logging information object
        params = {
            "images": images,
            "name": name,
            "RegisterationStatus": registeration_status
        }
        dbClient.Log("/admin/users/add", "POST", params, datetime.now())
        return jsonify(repsonse) # api request logs
    else:
        return "Invalid Request Method"

@app.route("/admin/user/update", methods=["POST"])
def adminUpdateUsers():
    if (request.method == "POST"):
        userId = request.get_json(force=True)["userId"] # docId to update
        params = request.get_json(force=True)["update"] # object values to update
        # api request logging information object
        dbClient.Log("/admin/user/update", "POST", params, datetime.now()) # api request logs
        return dbClient.Update("Users", userId, params) # returns True/False depending on if the document was updated
    else:
        return "Invalid Request Method"

@app.route("/personal/user/<userId>", methods=["GET"])
def getUser(userId):
    # if user id equal -1 return all users from database
    if (request.method == "GET"):
        if (userId != -1):
            return dbClient.ReadSingle(userId)
        else:
            return jsonify(dbClient.ReadAll())
    else:
        return "Invalid Request Method"


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")