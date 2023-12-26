import uvicorn
from fastapi import FastAPI


from app.api.auth_api import auth_router, register_router, reset_password_router, verify_router
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

app.include_router(
    reset_password_router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    verify_router,
    prefix="/auth",
    tags=["auth"]
)


