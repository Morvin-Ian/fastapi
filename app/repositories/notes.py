from .. import models
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from fastapi import HTTPException, status

def get_all(db:Session)->List[schemas.NoteResponse]:
    notes = db.query(models.Note).all()
    return notes

def get_note(note_id:int, db:Session)->List[schemas.NoteResponse]:
    note = db.query(models.Note).filter(models.Note.id==note_id ).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return note

def create(request:schemas.Note, db:Session)->schemas.NoteResponse:
    new_note = models.Note(title=request.title, description=request.description, user_id=1)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def update(note_id:int, request:schemas.Note, db:Session):
    note = db.query(models.Note).filter(models.Note.id==note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    note.update(request, synchronize_session=False)
    db.commit()
    return note

def delete(note_id:int, db:Session):
    note = db.query(models.Note).filter(models.Note.id==note_id )
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    note.delete(synchronize_session=False)
    db.commit()