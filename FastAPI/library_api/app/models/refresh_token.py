from datetime import datetime

from sqlalchemy import (Boolean, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    token_hash: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="refresh_tokens")