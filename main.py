from fastapi import FastAPI, Form, Body, APIRouter, Query, HTTPException 
from pydantic import BaseModel, Field
from typing import Optional

from data_models.schemas import  AsicsForm


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username,
            "logged_in": True }


@app.post("/register/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "password": password }

@app.post("/asicForm/")
async def create_asics_response(asics_form: AsicsForm):
    return asics_form


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


