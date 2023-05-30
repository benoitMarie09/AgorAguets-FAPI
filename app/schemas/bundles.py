from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, validator

if TYPE_CHECKING:
    from .formations import FormationBase


class BundleBase(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class BundleCreate(BundleBase):
    formations: list[int]


class BundleRead(BundleBase):
    id: int
    formations: list[FormationBase]
    price: float = None

    @validator("price", pre=True, always=True)
    def set_price(cls, v, values):
        return v or sum(formation.price for formation in values['formations'])


class BundleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    formations: Optional[list[int]] = None

    class Config:
        orm_mode = True
