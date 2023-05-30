from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.crud import get_row, save, get_rows, delete_row
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
    formations_db = get_rows(db, Formation, bundle.formations)
    db_bundle = models.Bundle(title=bundle.title, content=bundle.content)
    db_bundle.formations = formations_db
    save(db, db_bundle)
    return db_bundle


@router.get("/", response_model=list[schemas.BundleRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Bundle).offset(skip).limit(limit).all()


@router.get("/{bundles_id}", response_model=schemas.BundleRead)
def read_one(bundle_id: int, db: Session = Depends(get_db)):
    db_bundle = get_row(db, models.Bundle, bundle_id)
    return db_bundle


@router.delete("/{bundle_id}")
def delete(bundle_id: int, db: Session = Depends(get_db)):
    delete_row(db, models.Bundle, bundle_id)
    return {"Deleted": True}


@router.patch("/{bundle_id}", response_model=schemas.BundleRead)
def patch(bundle_id: int, bundle: schemas.BundleUpdate, db: Session = Depends(get_db)):
    db_bundle = get_row(db, Formation, bundle_id)
    bundle_data = bundle.dict(exclude_unset=True)
    for key, value in bundle_data.items():
        if key == "formations":
            formations_db = get_rows(db, models.Bundle, value)
            db_bundle.formations = formations_db
        else:
            setattr(db_bundle, key, value)
    save(db, db_bundle)
    return db_bundle


@router.put("/{bundle_id}", response_model=schemas.BundleRead)
def patch(bundle_id: int, bundle: schemas.BundleCreate, db: Session = Depends(get_db)):
    db_bundle = get_row(db, models.Bundle, bundle_id)
    for key, value in bundle.dict().items():
        if key == "formations":
            formations_db = get_rows(db, Formation, value)
            db_bundle.formations = formations_db
        else:
            setattr(db_bundle, key, value)
    save(db, db_bundle)
    return db_bundle




