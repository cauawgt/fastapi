from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_activate = Column(Boolean, default=True)
    role = Column(String)

# Inherit from 'Base' (defined in database.py) to tell SQLAlchemy this is a DB model.
class Todos(Base):
    # Define the table name as it appears in the database.
    __tablename__ = 'todos'

    # Define the columns (attributes) of the table.
    
    # 'id': Unique identifier for each todo. Primary Key means it's unique. 
    # Index=True makes searching by ID faster.
    id = Column(Integer, primary_key=True, index=True)

    # 'title' & 'description': Store text information about the task.
    title = Column(String)
    description = Column(String)

    # 'priority': An integer (e.g., 1-5) to sort importance.
    priority = Column(Integer)

    # 'complete': A True/False flag to track if the task is done. 
    # default=False means new tasks are incomplete by default.
    complete = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))