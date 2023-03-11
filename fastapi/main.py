from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hello(name: str): # http://127.0.0.1:8000/my-first-api?name=Rob
  return {'Hello ' + name + '!'} 
