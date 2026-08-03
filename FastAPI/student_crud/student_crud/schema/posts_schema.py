from pydantic import BaseModel, ConfigDict


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)