from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

# Initialize the FastAPI application.
app = FastAPI()

# Create the database tables.
# This looks at all models importing 'Base' (like Todos) and creates 
# the tables in 'todos.db' if they don't exist yet.
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
