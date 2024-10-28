from fastapi import (
    FastAPI, Depends, status,
    Response, HTTPException
)

from typing import List
from . import schemas, models
from .database import get_db, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(request)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/api/notes', status_code = status.HTTP_200_OK, response_model = List[schemas.NoteResponse])
def fetch_notes(db:Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

@app.get('/api/notes/{note_id}', status_code = status.HTTP_200_OK, response_model = schemas.NoteResponse)
def fetch_notes(note_id:int, db:Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==note_id ).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return note

@app.post('/api/notes', status_code = status.HTTP_201_CREATED)
async def create_note(request: schemas.Note, db: Session = Depends(get_db)):
    new_note = models.Note(title=request.title, description=request.description)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@app.put('/api/notes/{note_id}', status_code = status.HTTP_202_ACCEPTED)
def update_note(note_id:int, request:schemas.Note, db:Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    
    note.update(request, synchronize_session=False)
    db.commit()
    return {"success":"Note deleted"}

@app.delete('/api/notes/{note_id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int, db:Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==note_id )
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    
    note.delete(synchronize_session=False)
    db.commit()
    return {"success":"Note deleted"}