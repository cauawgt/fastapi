from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default = None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=11)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "name's author",
                "description": "A new description",
                "rating": 10,
            }
        }
    }