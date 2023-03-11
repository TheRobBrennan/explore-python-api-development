import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! This is a web app using Python Flask!'

@app.route('/my-first-api')
def hello():

    name = request.args.get('name')

    if name is None:
        text = 'Hello, world!'

    else:
        text = 'Hello, ' + name + '!'

    return jsonify({"message": text})

@app.route("/get-iris")
def get_iris():

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    # Note that we are converting our iris DataFrame to an object that can be converted to JSON - a dictionary, in this example.
    return jsonify({
        "message": "Iris Dataset",
        "data": iris.to_dict()
        })

# Start our server
app.run(debug=True, port=8000)
