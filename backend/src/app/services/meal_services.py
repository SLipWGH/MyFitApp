from datetime import date, time

from sqlalchemy import and_, cast, func, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.meal_models import MealIn, MealOut
from app.models.meal_models import Portion as PortionData
from app.tables import User, Meal, Portion, Food


async def post_meal_handler(
    session: AsyncSession,
    current_user: User,
    meal_data: MealIn,
):
    meal = create_meal(meal_data, session)
    current_user.meal.append(meal)
    await session.commit()
    return


async def create_meal(
    session: AsyncSession,
    meal_data: MealIn
) -> Meal:
    date, time, portions_data = meal_data.date, meal_data.time, meal_data.portions
    meal = Meal(date, time)
    meal.portions = create_portions(session, portions_data)
    session.add(meal)

    return meal


async def create_portions(
    session: AsyncSession,
    portions_data: list[PortionData],
) -> list[Portion]:
    portions = []
    for data in portions_data:
        mass = data.mass
        food_name = data.food_name
        portion = Portion(mass, food_name)
        portions.append(portion)
    session.add_all(portions)

    return portions 


async def insert_food(
    session: AsyncSession,
    food: set[Food]
) -> None:
    session.add_all(food)
    await session.commit()


async def get_food(
    session: AsyncSession,
    food_names: set[str]
):
    query = select(Food).where(Food.name.in_(food_names))
    result = await session.execute(query)

    return result
    

async def get_meal_handler(
    user: User
) -> MealOut:
    out = MealOut()
    out.date
    out.time
    out.portions
    out.total_carbohydrates
    out.total_proteins
    out.total_fats


# def get_register_router(
#     get_user_manager: UserManagerDependency[models.UP, models.ID],
#     user_schema: Type[schemas.U],
#     user_create_schema: Type[schemas.UC],
# ) -> APIRouter:
#     """Generate a router with the register route."""
#     router = APIRouter()

#     @router.post(
#         "/register",
#         response_model=user_schema,
#         status_code=status.HTTP_201_CREATED,
#         name="register:register",
#         responses={
#             status.HTTP_400_BAD_REQUEST: {
#                 "model": ErrorModel,
#                 "content": {
#                     "application/json": {
#                         "examples": {
#                             ErrorCode.REGISTER_USER_ALREADY_EXISTS: {
#                                 "summary": "A user with this email already exists.",
#                                 "value": {
#                                     "detail": ErrorCode.REGISTER_USER_ALREADY_EXISTS
#                                 },
#                             },
#                             ErrorCode.REGISTER_INVALID_PASSWORD: {
#                                 "summary": "Password validation failed.",
#                                 "value": {
#                                     "detail": {
#                                         "code": ErrorCode.REGISTER_INVALID_PASSWORD,
#                                         "reason": "Password should be"
#                                         "at least 3 characters",
#                                     }
#                                 },
#                             },
#                         }
#                     }
#                 },
#             },
#         },
#     )
#     async def register(
#         request: Request,
#         user_create: user_create_schema,  # type: ignore
#         user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
#     ):
#         try:
#             created_user = await user_manager.create(
#                 user_create, safe=True, request=request
#             )
#         except exceptions.UserAlreadyExists:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail=ErrorCode.REGISTER_USER_ALREADY_EXISTS,
#             )
#         except exceptions.InvalidPasswordException as e:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail={
#                     "code": ErrorCode.REGISTER_INVALID_PASSWORD,
#                     "reason": e.reason,
#                 },
#             )

#         return schemas.model_validate(user_schema, created_user)

#     return router




#     async def create(
#         self,
#         user_create: schemas.UC,
#         safe: bool = False,
#         request: Optional[Request] = None,
#     ) -> models.UP:
#         """
#         Create a user in database.

#         Triggers the on_after_register handler on success.

#         :param user_create: The UserCreate model to create.
#         :param safe: If True, sensitive values like is_superuser or is_verified
#         will be ignored during the creation, defaults to False.
#         :param request: Optional FastAPI request that
#         triggered the operation, defaults to None.
#         :raises UserAlreadyExists: A user already exists with the same e-mail.
#         :return: A new user.
#         """
#         await self.validate_password(user_create.password, user_create)

#         existing_user = await self.user_db.get_by_email(user_create.email)
#         if existing_user is not None:
#             raise exceptions.UserAlreadyExists()

#         user_dict = (
#             user_create.create_update_dict()
#             if safe
#             else user_create.create_update_dict_superuser()
#         )
#         password = user_dict.pop("password")
#         user_dict["hashed_password"] = self.password_helper.hash(password)

#         created_user = await self.user_db.create(user_dict)

#         await self.on_after_register(created_user, request)

#         return created_user
    
#         async def create(self, create_dict: Dict[str, Any]) -> UP:
#         user = self.user_table(**create_dict)
#         self.session.add(user)
#         await self.session.commit()
#         await self.session.refresh(user)
#         return user