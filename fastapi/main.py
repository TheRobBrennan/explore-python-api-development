from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

@app.get("/get-iris")
def get_iris():
    # When it comes to “normal” objects, like a DataFrame, FastAPI will convert it directly to a JSON file.
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris
