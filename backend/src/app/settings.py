import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession



load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
SECRET = os.environ.get("SECRET")
SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session(
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


cookie_transport = CookieTransport(cookie_name="cooka", cookie_max_age=3600)


def get_jwt_strategy(        
) -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="CJWT",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)
