# Todo API

An API-first ToDo list application built with FastAPI, PostgreSQL, and Docker — no frontend, just a clean RESTful API. Users own tasks in a one-to-many relationship, with UUID primary keys, SQLAlchemy models, and Alembic-managed migrations. Fully containerized via Docker Compose for consistent local setup.

**Setup:** `cp .env.example .env`, fill in credentials, then `docker compose up --build` followed by `docker compose exec web alembic upgrade head` to create the tables. API runs at `localhost:8000`, with interactive docs at `/docs`.