from fastapi.responses import JSONResponse


def success_response(message: str, data: object | None = None, status_code: int = 200) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"message": message, "data": data})
