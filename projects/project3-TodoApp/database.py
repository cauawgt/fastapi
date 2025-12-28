from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the location of the database file. 
# 'sqlite:///' tells SQLAlchemy we are using SQLite. 
# './todos.db' means the file is in the current directory.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# Create the engine. This is the starting point for any SQLAlchemy application.
# 'check_same_thread': False is specific to SQLite in FastAPI to allow 
# multiple threads to interact with the single database file safely.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a SessionLocal class. 
# This is a factory! Each time we instantiate this, we get a new database session.
# autocommit=False: We manually commit changes to be safe.
# autoflush=False: We manually flush changes to the DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class.
# Later, in models.py, our database models will inherit from this class 
# so SQLAlchemy knows they are tables in our database.
Base = declarative_base()