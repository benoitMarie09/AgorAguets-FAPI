from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import TypeVar

T = TypeVar('T')


def get_row(db: Session, model: T, model_id: int) -> T:
    db_row = db.query(model).filter(model.id == model_id).first()
    if not db_row:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found with id:{model_id}")
    return db_row


def get_rows(db: Session, model: T, models_ids: list[int]) -> list[T]:
    db_rows = [get_row(db, model, model_id) for model_id in models_ids]
    return db_rows


def delete_row(db: Session, model: T, model_id: int):
    db_row = get_row(db, model, model_id)
    db.delete(db_row)
    db.commit()


def patch_row(db: Session, schema: BaseModel, model: T, model_id: int) -> T:
    db_row = get_row(db, model, model_id)
    patch_data = schema.dict(exclude_unset=True)
    for key, value in patch_data.items():
        setattr(db_row, key, value)
    save(db, db_row)
    return db_row


def put_row(db: Session, schema: BaseModel, model: T, model_id: int) -> T:
    db_row = get_row(db, model, model_id)
    for key, value in schema.dict().items():
        setattr(db_row, key, value)
    save(db, db_row)
    return db_row


def save(db: Session, row : object):
    db.add(row)
    db.commit()
    db.refresh(row)
