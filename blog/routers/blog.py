from .. import schemas,models,database,hash
from typing import List
from fastapi import FastAPI,Depends, status,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
from .. repository import blog
from . import Oauth2
router=APIRouter(
    tags=["Blogs"],
    prefix="/blog",
)

get_db=database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
def creat(request: schemas.Blog, db:Session=Depends(get_db), current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return blog.getId(id,db)

@router.get('/',response_model=List[schemas.ShowBlog])
def show(db:Session=Depends(get_db), current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return blog.getAll(db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def up(id,request:  schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return blog.update(id,request,db)
    
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth2.get_current_user)):
    return blog.delete(id,db)