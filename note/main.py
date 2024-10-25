from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Note(BaseModel):
    title: str
    body: str
    completed

@app.post('/api/v1/create')
async def create_note(note: Note):
    return {"message": "Note created successfully"}
