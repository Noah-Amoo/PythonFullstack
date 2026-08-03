from typing import Optional, Annotated
from pydantic import BaseModel, Field

class ItemPayload(BaseModel):
    item_id: Annotated[Optional[int], Field(default=None, ge=0)]
    item_name: Optional[str]
    quantity: Annotated[Optional[int], Field(gt=0)]
    # Create another item and try to make it optional

    ## Also study on subdepencies


