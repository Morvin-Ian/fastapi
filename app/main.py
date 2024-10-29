from fastapi import FastAPI
from .database import  init_db
from .routers import notes, users, auth

init_db()
app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(notes.router)





