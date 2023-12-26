from datetime import date, time, timedelta
from typing import Annotated, Optional, List

from fastapi_users import schemas
from pydantic import BaseModel, Field


class ExerciseSet(BaseModel):
    # number: int
    burder_weight: int
    repetitions_count: int


class Exercise(BaseModel):
    name: str
    sets: List[ExerciseSet]


class BaseWorkout(BaseModel):
    date: date
    time: time
    duration: timedelta
    exercises: List[Exercise]



