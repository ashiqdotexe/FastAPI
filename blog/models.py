from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import Relationship

class Blog(Base):
    __tablename__= 'blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer, ForeignKey('user.id'))
    
    #relashionship part--
    creator=Relationship('User', back_populates='blog')
class User(Base):
    __tablename__='user'
    
    id=Column(Integer,primary_key=True,index=True)
    userName=Column(String)
    email =Column(String)
    password=Column(String)
    #relationship part
    blog=Relationship('Blog', back_populates='creator')
    
