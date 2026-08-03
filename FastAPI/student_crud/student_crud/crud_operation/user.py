from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user_models import UserCreate, UserResponse
from models.user import User
from database import get_db

router = APIRouter()


@router.post("/create_user/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:

    # Check if the username is empty
    if not user.username.strip():
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty."
        )

    # Check if the email is valid
    if user.email and "@" not in user.email:
        raise HTTPException(
            status_code=400,
            detail="Invalid email address."
        )

    # Check if username already exists
    existing_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )

    # Create SQLAlchemy model
    db_user = User(
        username=user.username,
        email=user.email
    )

    # Save to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserResponse.model_validate(db_user)


@router.get("/get_all_users/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    users = db.query(User).all()
    return [UserResponse.model_validate(user) for user in users]