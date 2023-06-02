## Subscribe API

API to manage Subscriber email.

## Setup `dev.env`
- Please rename `temp.env` to `dev.env`.
- Ensure that the `XXAPI` value is set and contains at least `16 characters`.
- The `XXAPI` value is required to protect your API endpoint.

#### Requirements

```bash
fastapi
pydantic
uvicorn
alembic
python-dotenv
sqlalchemy==1.4.35
asyncpg==0.26.0
pytz
ua_parser
```

#### Docker Setup

```bash
docker compose up
```
#### Init Migrations

```bash
alembic init migrations
```

#### Autogenerate Migrations
```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

#### Create DB
```bash
alembic upgrade head
```

#### Docker Exec

```bash
docker exec -w /myapp/app/v1 <container_ID> alembic upgrade head
```