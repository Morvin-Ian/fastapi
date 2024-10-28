from pydantic import BaseModel

class Note(BaseModel):
    title: str
    body: str
    completed: bool