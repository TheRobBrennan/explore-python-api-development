from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! This is a web app using Python Flask!'

# Start our server
app.run(debug=True, port=8000)