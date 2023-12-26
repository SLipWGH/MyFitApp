from enum import Enum
from typing import Annotated, Optional, Literal

from pydantic import Field
from fastapi_users import schemas


Gender = Literal["FEMALE", "MALE"]


class UserRead(schemas.BaseUser[int]):
    name: Annotated[str, Field(min_length=1, max_length=256)]
    surname: Annotated[str, Field(min_length=1, max_length=256)]
    lastname: Annotated[str, Field(min_length=1, max_length=256)]
    weight: Annotated[float | None, Field(
        gt=0., description="The weight must be greater than zero")] = None
    height: Annotated[float | None, Field(
        gt=0., description="The weight must be greater than zero")] = None
    age: Annotated[float | None, Field(gt=0)]
    gender: Gender
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    email: Annotated[str, Field(min_length=1, max_length=320)]


class UserCreate(schemas.BaseUserCreate):
    name: Annotated[str, Field(min_length=1, max_length=256)]
    surname: Annotated[str, Field(min_length=1, max_length=256)]
    lastname: Annotated[str, Field(min_length=1, max_length=256)]
    weight: Annotated[float | None, Field(
        gt=0., description="The weight must be greater than zero")] = None
    height: Annotated[float | None, Field(
        gt=0., description="The weight must be greater than zero")] = None
    age: Annotated[float | None, Field(gt=0)]
    gender: Gender
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    email: Annotated[str, Field(min_length=1, max_length=320)]
    password: Annotated[str, Field(min_length=8)]

class UserUpdate(schemas.BaseUserUpdate):
    pass


