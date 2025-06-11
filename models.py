# Import necessary libraries and modules
from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# Define a User model
class User(Base):
    # Define the name of the database table for this model
    __tablename__ = "users"

    # Define the columns for the users table
    id = Column(Integer, primary_key=True, index=True)
    # The username column is unique, meaning no two users can have the same username
    username = Column(String(50), unique=True)

# Define a Post model
class Post(Base):
    # Define the name of the database table for this model
    __tablename__ = 'posts'

    # Define the columns for the posts table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    # The user_id column is a foreign key that references the id column in the users table
    user_id = Column(Integer)