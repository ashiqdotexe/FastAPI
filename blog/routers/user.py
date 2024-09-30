from .. import schemas,models,database,hash
from typing import List
from fastapi import FastAPI,Depends, status,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    tags=["User"],
    prefix="/user"
)

get_db=database.get_db


#User part
@router.post('/')
def userInfo(request:schemas.User,db:Session=Depends(get_db)):
    return user.userInfo(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def userInfo(id,db:Session=Depends(get_db)):
    return user.getUser(id,db)

# @router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def deleteUser(id,db:Session=Depends(get_db)):
#     return user.deleteUser(id,db)
    