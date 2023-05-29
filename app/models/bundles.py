from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
#from .association_tables import bundles_formations

from app.database import Base


class Bundle(Base):
    __tablename__ = "bundles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String, index=True)
    formations = relationship("Formation", secondary="bundles_formations", back_populates="bundles")
