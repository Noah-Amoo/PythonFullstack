from fastapi import Request
from fastapi.responses import JSONResponse


# -----------------------------
# Custom Exceptions
# -----------------------------

class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "A user with this email already exists."


class InvalidCredentialsException(Exception):
    def __init__(self):
        self.message = "Invalid email or password."


class PermissionDeniedException(Exception):
    def __init__(self):
        self.message = "You do not have permission to perform this action."




# Exception Handlers
async def user_already_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException,
):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message},
    )


async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException,
):
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message},
    )


async def permission_denied_handler(
    request: Request,
    exc: PermissionDeniedException,
):
    return JSONResponse(
        status_code=403,
        content={"detail": exc.message},
    )