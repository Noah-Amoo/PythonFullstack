from passlib.context import CryptContext

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.core.config import settings

import secrets
import hashlib


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def create_refresh_token() -> str:
    """
    Generates a cryptographically secure random refresh token.
    """
    return secrets.token_urlsafe(64)


def hash_refresh_token(token: str) -> str:
    """
    Hashes a refresh token before storing it in the database.
    """
    return hashlib.sha256(token.encode()).hexdigest()


def verify_refresh_token(token: str) -> str:
    """
    Returns the hash of a refresh token.
    """
    return hashlib.sha256(token.encode()).hexdigest()

def verify_access_token(token: str):
    try:
        payload = jwt.decode( token, settings.secret_key, algorithms=[settings.algorithm])

        email = payload.get("sub")
        role = payload.get("role")

        if email is None:
            raise JWTError()

        return {
            "email": email,
            "role": role,
        }

    except JWTError:
        raise ValueError("Invalid token")