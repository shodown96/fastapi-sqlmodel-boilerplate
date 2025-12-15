import uuid
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: str = Field()
    name: str = Field()
    disabled: bool = Field(default=False)
    password: str = Field()
