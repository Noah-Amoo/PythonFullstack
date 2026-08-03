from typing import Optional
from fastapi import FastAPI, HTTPException
from models import ItemPayload
from pydantic import BaseModel

from database import engine
import roles

from users import Users

app = FastAPI()
roles.Base.metadata.create_all(bind=engine)

grocery_list: dict[int, ItemPayload] = {}

# Route to add an item
@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int) -> dict[str, ItemPayload]:
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    # if item already exists, we'll just add the quantity.
    # get all item names
    items_ids: dict[str, int] = {
        item.item_name: item.item_id if item.item_id is not None else 0
        for item in grocery_list.values()
    }
    if item_name in items_ids.keys():
        # get index of item_name in item_ids, which is the item_id
        item_id: int = items_ids[item_name]
        grocery_list[item_id].quantity += quantity
    # otherwise, create a new item
    else:
        # generate an ID for the item based on the highest ID in the grocery_list
        item_id: int = max(grocery_list.keys()) + 1 if grocery_list else 0
        grocery_list[item_id] = ItemPayload(
            item_id=item_id, item_name=item_name, quantity=quantity
        )
 
    return {"item": grocery_list[item_id]}

# Function to Read (Get) all items
@app.get("/items")
def read_items():
    if grocery_list == {}:
        raise HTTPException(status_code=400, detail="Items list is empty")
    return grocery_list

# Function to Read (Get) an item based on ID
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int) -> dict[str, ItemPayload]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": grocery_list[item_id]}

# Function to Update an item in the list
class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: ItemUpdate) -> dict[str, ItemPayload]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found")
    
    current_item = grocery_list[item_id]

    if updated_item.item_name is not None:
        current_item.item_name = updated_item.item_name

    if updated_item.quantity is not None:
        if updated_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be greater than zero")
        current_item.quantity = updated_item.quantity

    grocery_list[item_id] = current_item
    return {"item": current_item}

# Function to Delete an Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = grocery_list.pop(item_id)
    return {"message": f"Deleted {deleted_item.item_name} successfully"}
 

@app.post("/users")
def create_user(user: Users):
    return {"user": user}

@app.get("/")
def root():
    return {"message": "Hello World"}