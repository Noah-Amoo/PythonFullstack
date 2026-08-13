from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Lambda!"}

# This handler variable is what AWS Lambda will invoke
handler = Mangum(app)
