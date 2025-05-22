from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my the world of Chinmay Chatterjee"}

@app.get("/posts")
def get_posts():
    return{"data":"This is your posts"}

@app.post("/createposts")
def createpost(payload : dict=Body(...)):
    print(payload)
    return{"new_post":f"title:{payload['title']} content:{payload['content']}"}


