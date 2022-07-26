import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy

app= FastAPI()
"""
usernme
email
created_at
updated_at
"""
class User(BaseModel):
    username:str
    email:str
    # created_at:datetime.datetime
    # updated_at:datetime.datetime




class Poll(BaseModel):
    title:str
    type:str
    is_add_choices_active:bool
    is_voting_active:bool
    created_by:int
    # created_at:datetime.datetime
    # updated_at:datetime.datetime


@app.get("/")
async def root():
    return {"message":"Hello Zahra!"}

@app.get("/polls")
async def root():
    return {"polls":"Hello Zahra!"}


@app.get("/users")
async def root():
    return {"users":"Hello Zahra!"}



@app.post("/users")
async def create_user(user:User):
    return user

@app.post("/polls")
async def create_poll(poll:Poll):
    return poll