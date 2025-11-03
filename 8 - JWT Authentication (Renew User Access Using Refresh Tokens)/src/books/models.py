from sqlmodel import SQLModel, Field, Column, Date
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime, date


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
         pg.UUID,
         nullable=False,
         primary_key=True
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date = Field(sa_column=Column(pg.DATE))
    page_count: int
    language: str
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(pg.TIMESTAMP)
        )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(pg.TIMESTAMP)
        )

    def __repr__(self):
        return f"<Book {self.title}"
