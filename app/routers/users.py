from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    prefix="/api/users",
    tags = ["Users"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(password=request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==user_id ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return user