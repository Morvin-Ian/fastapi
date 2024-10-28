from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repositories import users

router = APIRouter(
    prefix="/api/users",
    tags = ["Users"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    return users.create(request, db)

@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    return users.get_one(user_id, db)