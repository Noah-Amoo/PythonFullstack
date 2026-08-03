from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.services.redis import get_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await get_redis().aclose()


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Redis Demo Auth API"}