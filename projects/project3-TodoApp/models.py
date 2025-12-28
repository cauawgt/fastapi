from database import Base
from sqlalchemy import Column, Integer, String, Boolean

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