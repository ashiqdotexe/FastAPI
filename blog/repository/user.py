from .. import schemas,models,hash
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def userInfo(request:schemas.User,db:Session):
    new_user=models.User(userName=request.userName, email=request.email,password=hash.Hashing.bcrypt2(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def getUser(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not found with the id {id}")
    return user

# def deleteUser(id:int,db:Session):
#     dele=db.query(models.User).filter(models.User.id==id).first()
#     if not dele:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'No content {id}')
    
#     db.commit()
#     return "Deleted"