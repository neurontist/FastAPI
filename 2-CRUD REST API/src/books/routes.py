from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.books_data import books
from src.books.schemas import BOOK, BOOKUpdate


router = APIRouter()


@router.get('/', response_model=List[BOOK])
async def get_all_books():
    return books

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book: BOOK) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book
    

@router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    for i in range(len(books)):
        if book_id == books[i]["id"]:
            return books[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
        )

@router.patch('/{book_id}') 
async def update_book(book_id: int, book_data: BOOKUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["publisher"] = book_data.publisher
            book["page_count"] = book_data.page_count
            book["language"] = book_data.language
        
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    

@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
