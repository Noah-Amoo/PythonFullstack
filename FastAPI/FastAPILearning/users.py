from typing import Optional, Annotated
from pydantic import BaseModel, Field

class Users(BaseModel):
    firstname: Annotated[str, Field(min_length=3, max_length=30)]
    lastname: Annotated[str, Field(min_length=2, max_length=15)]
    password: Annotated[str, Field(pattern=r"")]
    age: Annotated[Optional[int], Field(gt=0, lt=100)]





