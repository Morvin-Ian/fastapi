from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    email: str
    password: str

class Note(BaseModel):
    title: str
    description: str


class UserResponse(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class NoteResponse(Note):
    created_by: UserResponse

    class Config():
        orm_mode = True
    
