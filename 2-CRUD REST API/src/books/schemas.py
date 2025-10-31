from pydantic import BaseModel

class BOOK(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BOOKUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

