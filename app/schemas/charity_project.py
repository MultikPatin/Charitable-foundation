from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, Extra, validator, PositiveInt


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid

    @validator("description")
    def name_cannot_be_null(cls, value):
        if value == "":
            raise ValueError("Описание проекта не может быть пустым!")
        return value


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str
    full_amount: PositiveInt

    @validator("full_amount")
    def name_cannot_be_null(cls, value):
        if value < 1:
            raise ValueError("Сумма пожертвования не может быть менее 1!")
        return value


class CharityProjectCheckedCreate(CharityProjectCreate):
    invested_amount: int
    fully_invested: Optional[bool]
    close_date: Optional[datetime]


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    @validator("name")
    def name_cannot_be_null(cls, value):
        if value == "":
            raise ValueError("Имя проекта не может быть пустым!")
        return value


class CharityProjectCheckedUpdate(CharityProjectUpdate):
    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    close_date: Optional[datetime]
