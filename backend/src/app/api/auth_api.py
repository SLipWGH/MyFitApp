from app.models.auth_models import UserCreate, UserRead, UserUpdate
from app.services.auth_services import auth_backend, fastapi_users


auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
reset_password_router = fastapi_users.get_reset_password_router()
users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
verify_router = fastapi_users.get_verify_router(UserRead)

