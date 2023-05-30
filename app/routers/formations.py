from fastapi import APIRouter, Depends

from app.crud import save, delete_row, get_row
from app.schemas import formations as schemas
from app.models import formations as models
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(
    prefix="/formations",
    tags=["formations"],
)


@router.post("/", response_model=schemas.FormationRead)
def create(formation: schemas.FormationCreate, db: Session = Depends(get_db)):
    db_formation = models.Formation(
        title=formation.title,
        content=formation.content,
        price=formation.price,
    )
    save(db, db_formation)
    return db_formation


@router.get("/", response_model=list[schemas.FormationRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Formation).offset(skip).limit(limit).all()


@router.get("/{formation_id}", response_model=schemas.FormationRead)
def read_one(formation_id: int, db: Session = Depends(get_db)):
    db_formation = get_row(db, models.Formation, formation_id)
    return db_formation


@router.delete("/{formation_id}")
def delete(formation_id: int, db: Session = Depends(get_db)):
    delete_row(db, models.Formation, formation_id)
    return {"Deleted": True}


@router.patch("/{formation_id}", response_model=schemas.FormationRead)
def patch(formation_id: int, formation: schemas.FormationUpdate, db: Session = Depends(get_db)):
    db_formation = get_row(db, models.Formation, formation_id)
    formation_data = formation.dict(exclude_unset=True)
    for key, value in formation_data.items():
        setattr(db_formation, key, value)
    save(db, db_formation)
    return db_formation


@router.put("/{formation_id}", response_model=schemas.FormationRead)
def patch(formation_id: int, formation: schemas.FormationUpdate, db: Session = Depends(get_db)):
    db_formation = get_row(db, models.Formation, formation_id)
    for key, value in formation.dict().items():
        setattr(db_formation, key, value)
    save(db, db_formation)
    return db_formation
