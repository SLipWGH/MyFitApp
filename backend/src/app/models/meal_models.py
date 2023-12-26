from datetime import date, time
from typing import Annotated, Optional, List

from fastapi_users import schemas
from pydantic import BaseModel, Field

  
class Food(BaseModel):
    name: str
    proteins: float
    fats: float
    carbohydrates: float

    class Config:
        orm_mode = True


class Portion(BaseModel):
    mass: int
    food_name: str

    class Config:
        orm_mode = True


class BaseMeal(BaseModel):
    date: date
    time: time
    portions: List[Portion]

    class Config:
        orm_mode = True

class MealIn(BaseMeal):
    pass


class MealOut(BaseMeal):
    total_proteins: float
    total_fats: float
    total_carbohydrates: float









