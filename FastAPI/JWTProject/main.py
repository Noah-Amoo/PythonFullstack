from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def create_user():
    pass
    