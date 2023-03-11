from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! This is a web app using Python Flask!'

@app.route('/my-first-api')
def hello():

    name = request.args.get('name')

    if name is None:
        text = 'Hello world!'

    else:
        text = 'Hello ' + name + '!'

    return text

# Start our server
app.run(debug=True, port=8000)
