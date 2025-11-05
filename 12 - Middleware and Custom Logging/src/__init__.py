from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from .errors import register_all_errors
from .middleware import register_middleware

@asynccontextmanager
async def life_span(app: FastAPI):
    print('Server is starting...')
    await init_db()
    yield
    print('Server has stopped..')


app = FastAPI()

register_all_errors(app)
register_middleware(app)

app.include_router(router, prefix="/books", tags=['books'])
app.include_router(auth_router, prefix="/auth", tags=['auth'])
app.include_router(review_router, prefix="/review", tags=['review'])
app.include_router(tags_router, prefix="/tag", tags=['tags'])