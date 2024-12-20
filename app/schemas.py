from pydantic import BaseModel
from typing import List, Optional

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
    notes: List[Note]

    class Config():
        orm_mode = True

class NoteResponse(Note):
    created_by: UserResponse

    class Config():
        orm_mode = True
    
class LoginRequest(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None