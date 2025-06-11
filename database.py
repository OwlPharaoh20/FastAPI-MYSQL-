# Import necessary libraries and modules
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from the .env file
load_dotenv()

# Access the environment variable for the database password
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Construct the URL for the database connection
# This URL includes the username, password, host, port, and database name
URL_DATABASE = f'mysql+pymysql://root:{DB_PASSWORD}@localhost:3306/blogapplication'

# Create a database engine using the constructed URL
engine = create_engine(URL_DATABASE)

# Create a session maker for the database engine
# This session maker will be used to create new sessions for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
# This base class will be used to define the structure of the database tables
Base = declarative_base()