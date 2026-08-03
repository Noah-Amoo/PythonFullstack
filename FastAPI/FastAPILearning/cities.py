from typing import Optional, Annotated
from pydantic import RootModel, BaseModel, Field

class Cities:
    

# class Cities(BaseModel):
#     item_id: Annotated[Optional[int], Field(default=None, ge=0)]
#     item_name: Optional[str]
#     quantity: Annotated[Optional[int], Field(gt=0)]
    # Create another item and try to make it optional

    ## Also study on subdepencies






{
“Delhi” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Mumbai” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Hydrabad” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Jammu” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Nagpur” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Manchester” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
“Brazil” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500}
}