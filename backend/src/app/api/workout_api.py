from fastapi import APIRouter, Depends

from tables import User
from app.services.auth_services import current_user

workout_router = APIRouter()


@workout_router.get()
async def get_workout(
    user: User = Depends(current_user)
):
    pass


@workout_router.post()
async def post_workout(
    user: User = Depends(current_user)
):
    pass


