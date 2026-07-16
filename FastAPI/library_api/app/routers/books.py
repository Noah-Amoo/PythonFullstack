from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.dependencies.permissions import require_roles
from app.models.user import User, UserRole

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)

@router.get("/")
async def get_books(
    current_user: User = Depends(get_current_user),
):
    return {
        "message": f"Welcome {current_user.username}",
        "books": [
            "Clean Code",
            "FastAPI",
            "Python Tricks",
        ],
    }

@router.post("/")
async def add_book(
    current_user: User = Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.LIBRARIAN,
        )
    ),
):
    return {
        "message": "Book added successfully."
    }


@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    current_user: User = Depends(
        require_roles(UserRole.ADMIN)
    ),
):
    return {
        "message": f"Book {book_id} deleted."
    }