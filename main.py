from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

# Path Parameters
@app.get('/')
def root():
    return "hey"


@app.get('/about')
def root():
    return {'data':{'this the about'}}


@app.get('/contact/unsub')
def contact():
    return {"id is: ": "unsub"}


@app.get('/contact/{id}')
def contact(id: int):
    return {"id is: ": id}

# Query Parameters
@app.get('/blog')
def blog(limit=10, published:bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {f'{limit} book is published'}
    else:
        return {f'{limit} books'}
    # http://localhost:8000/blog?limit=50&published=false


# Request Body
class Blog(BaseModel):
    title: str
    body: str
    published: bool | None=None
    
@app.post('/blog')
def create_blog(blog: Blog):
    return (f"Blog is created with the title {blog.title}")
    