from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item : str


class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "exemple": {
                "item": "Read the next chapiter of the book"
            }
        }