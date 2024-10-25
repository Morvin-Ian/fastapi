from fastapi import FastAPI
from . import schemas


app = FastAPI()


@app.post('/api/v1/create')
async def create_note(note: schemas.Note):
    return {"message": "Note created successfully"}
