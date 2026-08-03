from fastapi import FastAPI

from database import init_db
from routers import router

from mangum import Mangum

app = FastAPI(title="Simple Auth Demo")
app.include_router(router)


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/")
def read_root():
    return {"message": "Auth demo is running"}

handler = Mangum(app)