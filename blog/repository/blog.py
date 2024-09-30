from .. import schemas,models
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

def create(blog:schemas.Blog,db:Session):
    new_db=models.Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_db)
    db.commit()
    db.refresh(new_db)
    return new_db

def getId(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"Blog with id {id} is not found")
    return blog

def getAll(db:Session):
    blog=db.query(models.Blog).all()
    return blog

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such blog with id {id}")
    blog.update(request.dict())
    db.commit()
    return "Updated"

def delete(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No such blog with id {id}")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted"