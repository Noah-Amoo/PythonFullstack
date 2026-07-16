from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.database.base import Base
from app.database.database import engine
from app.models.user import User
from app.models.refresh_token import RefreshToken

from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    PermissionDeniedException,
    user_already_exists_handler,
    invalid_credentials_handler,
    permission_denied_handler,
)

from app.core.middleware import log_requests, add_process_time_header
from starlette.middleware.base import BaseHTTPMiddleware

from app.routers.auth import router as auth_router
from app.routers.books import router as books_router


#The create_all was useful when Alembic had not been implemented.
# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await create_db()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)

app.add_exception_handler(InvalidCredentialsException, invalid_credentials_handler)

app.add_exception_handler(PermissionDeniedException, permission_denied_handler)

app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests)

app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)


app.include_router(auth_router)

app.include_router(books_router)