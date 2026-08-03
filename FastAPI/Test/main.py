from typing import List

from fastapi import FastAPI, Form
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
	name: str
	description: str | None = None
	price: float


items_db: dict[Item] = []


@app.get("/")
def read_root() -> dict[str, str]:
	return {"message": "Home"}


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
	return items_db


@app.post("/items/json", response_model=Item)
def create_item_json(item: Item) -> Item:
	items_db.append(item)
	return item


@app.post("/items/form", response_model=Item)
def create_item_form(
	name: str = Form(...),
	description: str | None = Form(None),
	price: float = Form(...),
) -> Item:
	item = Item(name=name, description=description, price=price)
	items_db.append(item)
	return item
