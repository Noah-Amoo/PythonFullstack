from typing import Optional, Annotated
from pydantic import BaseModel, Field


class ItemPayload(BaseModel):
    
    age: Annotated[int, Field(gt=0, lt=30)]  # Use Annotated with  conint to enforce age constraints
    ni_number: Annotated[
        Optional[str],
        Field(pattern=r"^[A-Z]{2}\d{6}[A-D]$")
    ] = None


class StudentPayload(ItemPayload):
    id: Optional[int] = None
    student_name: str





# {
# “Delhi” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Mumbai” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Hydrabad” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Jammu” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Nagpur” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Manchester” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500},
# “Brazil” {“NewYork”: 5000, “London”: 3500, “Norway”: 4500}
# }


class city_name(BaseModel):
    NewYork: int
    London: int
    Norway:int


class Country(BaseModel):
    country_name: city_name
