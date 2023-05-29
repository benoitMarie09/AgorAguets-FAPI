from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.models import bundles as models
from app.schemas import bundles as schemas
from sqlalchemy.orm import Session
from app.models.formations import Formation
from app.database import get_db

router = APIRouter(
    prefix="/bundles",
    tags=["bundles"],
)


@router.post("/", response_model=schemas.BundleRead)
def create(bundle: schemas.BundleCreate, db: Session = Depends(get_db)):
    stmt = select(Formation).where(Formation.id.in_(bundle.formations))
    formations_db = db.query(Formation).from_statement(stmt).all()
    db_bundle = models.Bundle(title=bundle.title, content=bundle.content)
    db_bundle.formations = formations_db
    db.add(db_bundle)
    db.commit()
    db.refresh(db_bundle)
    print(db_bundle)
    return db_bundle


@router.get("/", response_model=list[schemas.BundleRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_bundles = db.query(models.Bundle).offset(skip).limit(limit).all()
    if not db_bundles:
        raise HTTPException(status_code=404, detail="No bundles where found")
    return db_bundles


@router.get("/{bundles_id}", response_model=schemas.BundleRead)
def read_one(bundle_id: int, db: Session = Depends(get_db)):
    db_bundle = db.query(models.Bundle).filter(models.Bundle.id == bundle_id).first()
    if not db_bundle:
        raise HTTPException(status_code=404, detail="Bundle was not found")
    return db_bundle


@router.delete("/{bundle_id}")
def delete(bundle_id: int, db: Session = Depends(get_db)):
    db_bundle = db.query(models.Bundle).filter(models.Bundle.id == bundle_id).first()
    if not db_bundle:
        raise HTTPException(status_code=404, detail="Bundle not found")
    db.delete(db_bundle)
    db.commit()
    return {"Deleted": True}




