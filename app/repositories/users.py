from .. import models
from sqlalchemy.orm import Session
from .. import schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request:schemas.User, db:Session):
    hashed_password = Hash.bcrypt(password=request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(user_id, db):
    user = db.query(models.User).filter(models.User.id==user_id ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return user