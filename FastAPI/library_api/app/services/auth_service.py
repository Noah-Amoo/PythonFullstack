from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password

from app.models.user import User, UserRole
from app.schemas.user import UserCreate

from app.core.exceptions import UserAlreadyExistsException

async def register_user(user: UserCreate, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise UserAlreadyExistsException()
    
    hashed_password = hash_password(user.password)

    db_user = User(
    username=user.username,
    email=user.email,
    hashed_password=hashed_password,
    role=UserRole.MEMBER,
    )

    db.add(db_user)

    await db.commit()
    await db.refresh(db_user)

    return db_user