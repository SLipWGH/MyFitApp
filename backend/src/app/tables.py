from datetime import date, time
from typing import Annotated, Literal, get_args

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Enum, ForeignKey, String, Boolean, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column, relationship



intpk = Annotated[int, mapped_column(primary_key=True)]
boolf = Annotated[bool, mapped_column(Boolean, default=False, nullable=False)]
str_256 = Annotated[str, mapped_column(String(256))]

Gender = Literal["FEMALE", "MALE"]


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user_account"

    id: Mapped[intpk]
    name: Mapped[str_256]
    surname: Mapped[str_256]
    lastname: Mapped[str_256]
    weight: Mapped[float] = mapped_column(nullable=True)
    height: Mapped[float] = mapped_column(nullable=True)
    age: Mapped[int]
    gender:Mapped[Gender] = mapped_column(
        Enum(*get_args(Gender), name="gender", create_constraints=True, validate_strings=True)
    )
    is_active: Mapped[boolf]
    is_superuser: Mapped[boolf]
    is_verified: Mapped[boolf]
    email: Mapped[str] = mapped_column(
    String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
    String(length=1024), nullable=False
    )
    meal: Mapped[list["Meal"]] = relationship()
    workout: Mapped[list["Workout"]] = relationship()


class Meal(Base):
    __tablename__ = "meal"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_account.id", ondelete="CASCADE")
    )
    date: Mapped[date]
    time: Mapped[time]
    portions: Mapped[list["Portion"]] = relationship()


class Food(Base):
    __tablename__ = "food"

    name: Mapped[str] = mapped_column(String(256), primary_key=True)
    proteins: Mapped[float]
    fats: Mapped[float]
    carbohydrates: Mapped[float]


class Portion(Base):
    __tablename__ = "portion"
    __table_args__ = (
        UniqueConstraint(
            "food_name",
            "meal_id",
            name="idx_unique_meal_food"
        ),
    )

    food_name: Mapped[str] = mapped_column(
        String(256),
        ForeignKey("food.name", onupdate="CASCADE"),
        primary_key=True
    )
    meal_id: Mapped[int] = mapped_column(
        ForeignKey("meal.id"),
        primary_key=True
    )
    mass: Mapped[float]
    food: Mapped["Food"] = relationship()


class Workout(Base):
    __tablename__ = "workout"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_account.id",ondelete="CASCADE")
    )
    date: Mapped[date]
    duration: Mapped[int]
    exercise_sets: Mapped[list["ExerciseSet"]] = relationship()


class Exercise(Base):
    __tablename__ = "exercise"

    name: Mapped[str] = mapped_column(String(256), primary_key=True)


class ExerciseSet(Base):
    __tablename__ = "exercise_set"

    id: Mapped[intpk]
    exercise_name: Mapped[str] = mapped_column(
        String(256), ForeignKey("exercise.name", onupdate="CASCADE")
    )
    workout_id: Mapped[int] = mapped_column(ForeignKey("workout.id", ondelete="CASCADE"))
    number: Mapped[int]
    burden_weight: Mapped[int]
    repetitions_count: Mapped[int]
    exercise: Mapped["Exercise"] = relationship()



