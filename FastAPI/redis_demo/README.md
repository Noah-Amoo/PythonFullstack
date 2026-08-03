# Redis Demo Auth

Simple FastAPI authentication demo using PostgreSQL for users and Redis for refresh-token/session storage.

## Setup

1. Install dependencies:
   `pip install -r requirements.txt`
2. Create a `.env` file from the example below and fill in your PostgreSQL database name.
3. Start Redis and PostgreSQL locally.
4. Run the migrations:
   `alembic upgrade head`
5. Run the API:
   `uvicorn app.main:app --reload`

## Environment

Create a `.env` file with:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_db_name

REDIS_URL=redis://localhost:6379/0
SECRET_KEY=change-me
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

## Endpoints

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/logout`
- `GET /api/v1/auth/me`

## Migrations

The initial Alembic revision creates the `users` table. After updating `POSTGRES_DB`, run `alembic upgrade head` to create the schema in your database.
