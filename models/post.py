import uuid
from datetime import datetime, timezone

from sqlmodel import Field, ForeignKey, SQLModel


# class Post(SQLModel, table=True):
#     id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
#     body: str = Field()
#     author: str = ForeignKey()
#     published: bool = Field(default=False)
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
