from fastapi import Depends, FastAPI

from app.routers import actualities, bundles, formations
from app.models import actualities as models_actualities
from app.models import bundles as models_bundles
from app.models import formations as models_formations
from .database import engine


models_actualities.Base.metadata.create_all(bind=engine)
models_bundles.Base.metadata.create_all(bind=engine)
models_formations.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(actualities.router)
app.include_router(bundles.router)
app.include_router(formations.router)

