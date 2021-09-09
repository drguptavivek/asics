from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def items():
    return {"message": "127.0.0.0:8000/items"}

# Item_id passed as Path Parameter of Type Integer
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Restricted set of users allowed as Path Parameters - using Enum
from enum import Enum
class Users(str, Enum):
    vivek = "Vivek"
    gupta = "Gupta"
    epidemiologist = "Epidemiologist"

@app.get("/users/{user_name}")
async def users(user_name: Users):
    return {"user": user_name}

# Both Path Parameter (item_id) and Query Parametrs: 
# needy, a required str.
# skip, an int with a default value of 0.
# limit, an optional int
from typing import Optional
@app.get("/items2/{item_id}")
async def read_user_item(
    item_id: str, 
    needy: str, 
    skip: int = 0, 
    limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# JSON Requesst Body
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/add_items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# Form Data
from fastapi import Form
@app.post("/login_form/")
async def loginForm(username: str = Form(...), password: str = Form(...)):
    return {"username": username,
            "logged_in": True }

# Files
from fastapi import UploadFile, File

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename,
            "content_type": file.content_type}

# Model Validation using Pydantic
