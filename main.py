# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

# Create a new FastAPI application
app = FastAPI()

# Create the database tables based on the models
models.Base.metadata.create_all(bind=engine)

# Define a base model for a post
class PostBase(BaseModel):
    # Define the fields for a post
    title: str
    content: str
    user_id: int

# Define a base model for a user
class UserBase(BaseModel):
    # Define the field for a user
    username: str

# Define a function to get a database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the database session
        yield db
    finally:
        # Close the database session
        db.close()

# Define a dependency for the database session
db_dependency = Annotated[Session, Depends(get_db)]

# Define a route to read all posts
@app.get("/posts/", status_code=status.HTTP_200_OK)
async def read_posts(db: db_dependency):
    # Query the database for all posts
    posts = db.query(models.Post).all()
    # Return the posts
    return posts

# Define a route to create a new post
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    # Create a new post object from the request data
    db_post = models.Post(**post.dict())
    # Add the post to the database
    db.add(db_post)
    # Commit the changes
    db.commit()

# Define a route to read a single post
@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    # Query the database for the post with the given ID
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    # If the post is not found, raise a 404 error
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    # Return the post
    return post

# Define a route to delete a post
@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    # Query the database for the post with the given ID
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    # If the post is not found, raise a 404 error
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    # Delete the post from the database
    db.delete(db_post)
    # Commit the changes
    db.commit()
    # Return a success message
    return {"message": "Post deleted successfully"}

# Define a route to create a new user
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    # Create a new user object from the request data
    db_user = models.User(**user.dict())
    # Add the user to the database
    db.add(db_user)
    # Commit the changes
    db.commit()

# Define a route to read a single user
@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    # Query the database for the user with the given ID
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # If the user is not found, raise a 404 error
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the user
    return user