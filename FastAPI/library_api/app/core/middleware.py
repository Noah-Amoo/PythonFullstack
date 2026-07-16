import time

from fastapi import Request

async def log_requests(request: Request, call_next):
    print("=" * 50)
    print(f"Incoming Request: {request.method} {request.url.path}")

    response = await call_next(request)

    print(f"Completed Response: {response.status_code}")
    print("=" * 50)

    return response


async def add_process_time_header(
    request: Request,
    call_next,
):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    return response