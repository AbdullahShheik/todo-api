from fastapi import FastAPI

from app.routes import users, tasks

app = FastAPI(title="Todo API")

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def health_check():
    return {"status": "ok"}
