from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import (verify_password, create_access_token, create_refresh_token, hash_refresh_token)

from app.database.database import get_db

from app.dependencies.auth import get_current_user

from app.models.refresh_token import RefreshToken
from app.models.user import User

from app.schemas.user import UserCreate
from app.services.auth_service import register_user



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    return await register_user(user, db)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    # OAuth2 uses "username" even when we're logging in with email.
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role.value,
        },
        expires_delta=timedelta(
            minutes=settings.access_token_expire_minutes
        ),
    )

    refresh_token = create_refresh_token()

    refresh_token_db = RefreshToken(
        token_hash=hash_refresh_token(refresh_token),
        user_id=user.id,
        expires_at=datetime.utcnow() + timedelta(days=7),
    )

    db.add(refresh_token_db)
    await db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh")
async def refresh(
    refresh_token: str,
    db: AsyncSession = Depends(get_db),
):
    token_hash = hash_refresh_token(refresh_token)

    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == token_hash,
            RefreshToken.is_revoked == False,
        )
    )

    stored_token = result.scalar_one_or_none()

    if stored_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    if stored_token.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token expired",
        )

    user = await db.get(User, stored_token.user_id)

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role.value,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.value,
        "is_active": current_user.is_active,
    }

@router.post("/logout")
async def logout(
    refresh_token: str,
    db: AsyncSession = Depends(get_db),
):
    token_hash = hash_refresh_token(refresh_token)

    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == token_hash
        )
    )

    stored_token = result.scalar_one_or_none()

    if stored_token is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Refresh token not found",
        )

    stored_token.is_revoked = True

    await db.commit()

    return {
        "message": "Logged out successfully"
    }

