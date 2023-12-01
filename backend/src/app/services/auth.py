from typing import Optional
from fastapi import Depends, Request
from fastapi_users import FastAPIUsers, IntegerIDMixin, BaseUserManager
from fastapi_users.schemas import UC
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.tables import User
from app.settings import auth_backend, get_async_session, SECRET, SECRET_KEY

class UserManager(IntegerIDMixin, BaseUserManager[User, NotImplementedError]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET_KEY


    async def on_after_register(
        self, 
        user: User, 
        request: Request | None = None
    ) -> None:
        print(f"User {user.id} has registered")


    async def create(
        self, 
        user_create: UC, 
        safe: bool = False,
        request: Request | None = None
    ) -> User:
        return await super().create(user_create, safe, request)


async def get_user_db(
    session: AsyncSession = Depends(get_async_session)
):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(
    user_db = Depends(get_user_db)
):
    yield UserManager(user_db)
    

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)




