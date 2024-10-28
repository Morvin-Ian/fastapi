from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Note(BaseModel):
    title: str
    description: str

class NoteResponse(Note):
    class Config():
        orm_mode = True
    
