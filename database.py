import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 


load_dotenv()  # loads environment variables from .env file

# access the environment variable
DB_PASSWORD = os.getenv('DB_PASSWORD')


URL_DATABASE = f'mysql+pymysql://root:{DB_PASSWORD}@localhost:3306/blogapplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

