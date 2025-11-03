from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import router
from src.auth.routes import auth_router

@asynccontextmanager
async def life_span(app: FastAPI):
    print('Server is starting...')
    await init_db()
    yield
    print('Server has stopped..')


app = FastAPI(
    lifespan=life_span
)

app.include_router(router, prefix="/books", tags=['books'])
app.include_router(auth_router, prefix="/auth", tags=['auth'])