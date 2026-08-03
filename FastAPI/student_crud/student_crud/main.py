
from controllers import posts, user
from fastapi import FastAPI, HTTPException
from typing import Optional
import controllers.student as student
import controllers.item as item
from models.student import Student  # Import the model
from models.user import User  # Import the model
from models.posts import Post  # Import the model
from database import Base
import controllers.posts as posts
import roles
from database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    item.router,
    prefix="/items",
    tags=["Items"]
)

app.include_router(
    user.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    posts.router,
    prefix="/posts",
    tags=["Posts"]
)