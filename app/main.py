from fastapi import FastAPI
from . import schemas, models
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post('/api/v1/create')
async def create_note(note: schemas.Note):
    return {"message": "Note created successfully"}
