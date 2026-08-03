from typing import Optional
from models.posts import Post
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[Optional[str]] = mapped_column(String(120))

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="owner"
    )