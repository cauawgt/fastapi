from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    email : str
    username: str
    first_name: str
    last_name: str
    password: str
    is_activate: bool
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str