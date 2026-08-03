from typing import Optional
from pydantic import BaseModel, conint

class ItemPayload(BaseModel):
    item_id: Optional[int] = None
    item_name: str
    quantity: conint(gt=0)  # type: ignore # quantity must be greater than 0