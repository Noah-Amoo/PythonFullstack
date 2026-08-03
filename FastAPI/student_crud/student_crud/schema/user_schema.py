

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: Optional[str]

    model_config = ConfigDict(from_attributes=True)