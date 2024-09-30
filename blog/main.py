from typing import List
from fastapi import FastAPI,Depends, status,HTTPException
from . import schemas,models,hash, database
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .routers import blog,user,authentication

app=FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
models.Base.metadata.create_all(engine)

 
        




