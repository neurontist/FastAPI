from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print('Server is starting...')
    await init_db()
    yield
    print('Server has stopped..')


app = FastAPI(
    lifespan=life_span
)