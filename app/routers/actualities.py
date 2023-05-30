from fastapi import APIRouter, Depends, HTTPException
from app.schemas.actualities import ActualityRead, ActualityCreate, ActualityUpdate
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import actualities as models
from app.crud import get_row, save, delete_row

router = APIRouter(
    prefix="/actualities",
    tags=["actualities"],
)


@router.post("/", response_model=ActualityRead)
def create(actuality: ActualityCreate, db: Session = Depends(get_db)):
    db_actuality = models.Actuality(**actuality.dict())
    save(db, db_actuality)
    return db_actuality


@router.get("/", response_model=list[ActualityRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Actuality).offset(skip).limit(limit).all()


@router.get("/{actuality_id}", response_model=ActualityRead)
def read_one(actuality_id: int, db: Session = Depends(get_db)):
    db_actuality = get_row(db, models.Actuality, actuality_id)
    return db_actuality


@router.delete("/{actuality_id}")
def delete(actuality_id: int, db: Session = Depends(get_db)):
    delete_row(db, models.Actuality, actuality_id)
    return {"Deleted": True}


@router.patch("/{actuality_id}", response_model=ActualityRead)
def patch(actuality_id: int, actuality: ActualityUpdate, db: Session = Depends(get_db)):
    db_actuality = get_row(db, models.Actuality, actuality_id)
    actuality_data = actuality.dict(exclude_unset=True)
    for key, value in actuality_data.items():
        setattr(db_actuality, key, value)
    save(db, db_actuality)
    return db_actuality


@router.put("/{actuality_id}", response_model=ActualityRead)
def put(actuality_id: int, actuality: ActualityCreate, db: Session = Depends(get_db)):
    db_actuality = get_row(db, models.Actuality, actuality_id)
    for key, value in actuality.dict().items():
        setattr(db_actuality, key, value)
    save(db, db_actuality)
    return db_actuality

