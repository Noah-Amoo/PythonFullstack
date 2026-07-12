from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, conint, constr, field_validator
from typing import Annotated

class User(BaseModel):
    username: Annotated[str, Field(regex=r'^[a-zA-Z0-9_.-]+$')]
    email: EmailStr
    age: Annotated[int, Field(gt=0)]

app = FastAPI()

@app.post("/register/")
async def register_user(user: User):
    return user