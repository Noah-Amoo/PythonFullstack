from fastapi import APIRouter


router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/")
async def get_books():
    return {"message": "Books router is working"}
    