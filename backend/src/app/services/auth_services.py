from typing import Any, Dict, Optional
from fastapi import Depends, Request, Response, HTTPException
from fastapi_users import FastAPIUsers, IntegerIDMixin, BaseUserManager
from fastapi_users.schemas import UC
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from pydantic import EmailStr, HttpUrl
from sqlalchemy.ext.asyncio import AsyncSession

from app.tables import User
from app.settings import auth_backend, get_async_session, SECRET, SECRET_KEY
from app.utils.email import send



class UserManager(IntegerIDMixin, BaseUserManager[User, NotImplementedError]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET_KEY
 

    async def on_after_register(
        self, 
        user: User, 
        request: Request | None = None
    ) -> None:
        print(f"User {user.id} has registered")

    
    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Request | None = None
    ) -> None:
        html = """\
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <title>Page Title</title>
                    <style type="text/css">
                    .h1, .p, .bodycopy {{color: #153643; font-family: sans-serif;}}
                    .h1 {{font-size: 33px; line-height: 38px; font-weight: bold;}}
                    </style>
                    </head>
                    <body>

                    <h1>Hi, {name}</h1>
                    <p>Here is very good frontend page with your token \n {token}.</p>

                    </body>
                    </html> 
                """.format(name=user.name, token=token)
        await send([user.email], html)

    
    async def on_after_reset_password(
        self,
        user: User,
        request: Request | None = None
    ) -> None:
        print(f"User {user.id} has reset password")
    
    
    async def on_after_request_verify(
        self, 
        user: User, 
        token: str, 
        request: Request | None = None
    ) -> None:
        html = """\
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <title>Page Title</title>
                    <style type="text/css">
                    .h1, .p, .bodycopy {{color: #153643; font-family: sans-serif;}}
                    .h1 {{font-size: 33px; line-height: 38px; font-weight: bold;}}
                    </style>
                    </head>
                    <body>

                    <h1>Hi, {name}</h1>
                    <p>Here is very good frontend page with your token \n {token}.</p>

                    </body>
                    </html> 
                """.format(name=user.name, token=token)
        await send([user.email], html)
    

    async def on_after_verify(
        self, 
        user: User, 
        request: Request | None = None
    ) -> None:
        print(f"User {user.id} has verified")
    


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

current_user = fastapi_users.current_user()


