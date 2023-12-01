from app.models.auth import UserCreate, UserRead, UserUpdate
from app.services.auth import auth_backend, fastapi_users


auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)


