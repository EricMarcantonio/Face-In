import base64 # for base64 decoding 
from flask import Flask, render_template, request # flask related 

app = Flask(__name__)

# DEFAULT ROUTE
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# RECIEVES IMAGE AS POST
# {
    # image: "base-64-encoded-image-data"
# }
@app.route("/image", methods=["GET", "POST"])
def getImage():
    if (request.method == "POST"): # checking if request is post
        image = request.get_json(force=True)["image"][22:] # removing descriptor for the data data:image/png;base64,
        with open("test_image.png", "wb") as f: # writing image to file in binary
            f.write(base64.b64decode(image)) # decoding image from base64
    
    return "" # depending on the response return a response 

if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")

