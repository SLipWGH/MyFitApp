from fastapi import FastAPI

from app.api.auth import auth_router, register_router
app = FastAPI()

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    register_router,
    prefix="/auth",
    tags=["auth"]
)

