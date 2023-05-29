from fastapi import APIRouter, Depends, HTTPException
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
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    return db_formation


@router.get("/", response_model=list[schemas.FormationRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_formations = db.query(models.Formation).offset(skip).limit(limit).all()
    if not db_formations:
        raise HTTPException(status_code=404, detail="No formations where found")
    return db_formations


@router.get("/{formation_id}", response_model=schemas.FormationRead)
def read_one(formation_id: int, db: Session = Depends(get_db)):
    db_formation = db.query(models.Formation).filter(models.Formation.id == formation_id).first()
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation was not found")
    return db_formation


@router.delete("/{formation_id}")
def delete(formation_id: int, db: Session = Depends(get_db)):
    db_formation = db.query(models.Formation).filter(models.Formation.id == formation_id).first()
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    db.delete(db_formation)
    db.commit()
    return {"Deleted": True}

