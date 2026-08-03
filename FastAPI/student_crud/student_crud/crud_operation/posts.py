from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.posts import Post
from models.user import User
from models.posts_models import PostCreate, PostResponse

router = APIRouter()


@router.post("/create_post/", response_model=PostResponse)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db)
) -> PostResponse:

    # Check if user exists
    user = db.query(User).filter(User.id == post.user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    # Create SQLAlchemy Post object
    db_post = Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return PostResponse.model_validate(db_post)

@router.get("/get_all_posts/", response_model=None)
def get_all_posts(db: Session = Depends(get_db)) -> list[PostResponse]:
    posts = db.query(Post).all()    
    return [PostResponse.model_validate(post) for post in posts]

@router.get("/get_posts_by_user/{user_id}/", response_model=list[PostResponse])
def get_posts_by_user(user_id: int, db: Session = Depends(get_db)) ->list[   PostResponse]:
        user = db.query(User).filter(User.id == user_id).first()
    
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )
    
        posts = db.query(Post).filter(Post.user_id == user_id).all()
        return [PostResponse.model_validate(post) for post in posts]        
