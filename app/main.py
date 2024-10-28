from fastapi import FastAPI, Depends
from . import schemas, models
from .database import get_db, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/api/v1/notes')
def fetch_notes(db:Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

@app.post('/api/v1/notes')
async def create_note(request: schemas.Note, db: Session = Depends(get_db)):
    new_note = models.Note(title=request.title, description=request.description)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
