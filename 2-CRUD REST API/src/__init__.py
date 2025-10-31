from fastapi import FastAPI
from src.books.routes import router

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A CRUD REST API App",
    version=version
)

app.include_router(router, prefix=f"/api/{version}/books", tags=['books'])