from .. import schemas,models,database,hash
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends, status,HTTPException

def login(request:schemas.Login,db:Session):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Username invalid")
    if hash.Hashing.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Password invalid")
    return user
        
    