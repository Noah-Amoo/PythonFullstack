from models.item_models import ItemPayload
from fastapi import HTTPException, APIRouter

router = APIRouter()
grocery_list: dict[int, ItemPayload] = {} # dictionary to store items with item_id as key and ItemPayload as value


@router.post("/{item_name}/{quantity}") # decorator to define a POST route with item_name and quantity as path parameters
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
 

@router.get("/grocery-list")  # decorator to define a GET route to retrieve the grocery list
def read_grocery_list(): 
    if grocery_list == {}:
        raise HTTPException(status_code=400, detail="Grocery list is empty.")
    
    return {"grocery_list": grocery_list}

