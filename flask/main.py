import pandas as pd

import io
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

from flask import Flask, request, jsonify, Response

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

@app.route("/plot-iris")
def plot_iris():

    # Create a buffer to hold the image
    img_buf = create_iris_image_buffer()

    # Set the buffer position to the start
    img_buf.seek(0)

    return Response(img_buf, mimetype='image/png')

def create_iris_image_buffer():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    # Create a 750px x 350px plot
    plt.rcParams['figure.figsize'] = [7.50, 3.50]
    plt.rcParams['figure.autolayout'] = True
    fig = plt.figure()  # make sure to call this, in order to create a new figure
    img_buf = io.BytesIO()
    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig(img_buf, format='png')
    plt.close(fig)
    return img_buf

# Start our server
app.run(debug=True, port=8000)
