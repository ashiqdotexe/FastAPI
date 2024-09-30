from .. import schemas,models,database
from ..hash import Hashing
from typing import List
from fastapi import FastAPI,Depends, status,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
from . import token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router=APIRouter(
    tags=["Authentication"],
    prefix="/login"
)
get_db=database.get_db
@router.post('/')
def login(request:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hashing.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Incorrect password")
        
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
