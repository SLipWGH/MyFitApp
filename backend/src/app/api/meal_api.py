from fastapi import APIRouter, Depends

from app.services.auth_services import current_user
from tables import User

meal_router = APIRouter()


@meal_router.get()
async def get_meal(
    user: User = Depends(current_user)
):
    pass


@meal_router.post()
async def post_meal(
    user: User = Depends(current_user)
):
    pass








