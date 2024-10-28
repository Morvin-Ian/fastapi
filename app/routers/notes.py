from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..repositories import notes
from .. import schemas, oauth
from ..database import get_db


router = APIRouter(
    prefix="/api/notes",
    tags = ["Notes"]
)

@router.get('/', status_code = status.HTTP_200_OK,  response_model = List[schemas.NoteResponse])
def fetch_notes(db:Session = Depends(get_db), get_current_user:schemas.User = Depends(oauth.get_current_user)):
    return notes.get_all(db)

@router.get('/{note_id}', status_code = status.HTTP_200_OK,  response_model = schemas.NoteResponse)
def fetch_note(note_id:int, db:Session = Depends(get_db))->schemas.NoteResponse:
    return notes.get_note(note_id, db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_note(request: schemas.Note, db: Session = Depends(get_db)):
    return notes.create(request, db)

@router.put('/{note_id}', status_code = status.HTTP_202_ACCEPTED)
def update_note(note_id:int, request:schemas.Note, db:Session = Depends(get_db)):
    return notes.update(note_id, request, db)

@router.delete('/{note_id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int, db:Session = Depends(get_db)):
    return notes.delete(note_id, db)

