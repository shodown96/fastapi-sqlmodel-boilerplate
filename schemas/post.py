from pydantic import BaseModel

class PostCreate(BaseModel):
    body: str