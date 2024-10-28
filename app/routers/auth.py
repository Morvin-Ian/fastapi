import os
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from typing import Annotated

from ..database import get_db
from .. import schemas, models
from ..hashing import Hash
from ..jwt import create_access_token

load_dotenv()

router = APIRouter(
    # prefix="/api/auth",
    tags=["Authentication"]
)

@router.post('/token', response_model=schemas.Token)
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(password=request.password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")