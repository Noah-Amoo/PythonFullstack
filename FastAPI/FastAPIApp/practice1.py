from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=100)

    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("Name must not be empty")
        return v

@app.post("/users/")
async def create_user(user: User):
    u= {"sender user": user.name, "senderage": user.age}
    return u

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    return {"name": "noah", "age": 36}