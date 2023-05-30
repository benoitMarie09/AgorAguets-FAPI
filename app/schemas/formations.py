from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel


if TYPE_CHECKING:
    from .bundles import BundleBase


class FormationBase(BaseModel):
    title: str
    content: str
    price: float

    class Config:
        orm_mode = True


class FormationCreate(FormationBase):
    bundles: list[int] | None = None


class FormationRead(FormationBase):
    id: int
    bundles: list[BundleBase] | None = None


class FormationUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True
