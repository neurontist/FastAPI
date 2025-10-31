from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"Hello World"}

@app.get('/greet_morning/{name}') # path parameter
async def morning(name: str) -> dict:
    return {"message":f"Good Morning {name}"}

@app.get('/greet_afternoon') # query parameter
async def afternoon(name: str) -> dict:
    return {"message":f"Good Afternoon {name}"}

@app.get('/greet_evening/{name}') # query and path param in the same endpoint
async def evening(name: str, age: int) -> dict:
    return {"message":f"Good Evening {name}", "age":age}

@app.get('/greet_night')
async def night(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message":f"Good Night {name}", "age":age}

class CREATE_BOOK(BaseModel):
    title: str
    author: str

@app.post('/create_book')
async def create_book(book: CREATE_BOOK):
    return {
        "title": book.title,
        "author": book.author
    }

@app.get('/get_header', status_code=200)
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    host: str = Header(None)
):
    return {
        "accept": accept,
        "content_type": content_type,
        "host": host
    }