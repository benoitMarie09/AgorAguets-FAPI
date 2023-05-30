from datetime import date
from typing import Optional

from pydantic import BaseModel


class ActualityBase(BaseModel):
    title: str
    content: str
    date: date

    class Config:
        orm_mode = True


class ActualityCreate(ActualityBase):
    pass


class ActualityRead(ActualityBase):
    id: int


class ActualityUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    date:  Optional[date]

    class Config:
        orm_mode = True

