from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool 

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new task",
                "description": "A new description",
                "priority": 5,
                "complete": False
            }
        }
    }