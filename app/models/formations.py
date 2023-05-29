from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
# from .association_tables import bundles_formations

from app.database import Base


bundles_formations = Table('bundles_formations', Base.metadata,
                           Column('bundle_id', ForeignKey('bundles.id'), primary_key=True),
                           Column('formation_id', ForeignKey('formations.id'), primary_key=True)
                           )


class Formation(Base):
    __tablename__ = "formations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String, index=True)
    price = Column(Float)
    duration = Column(Float)
    bundles = relationship("Bundle", secondary="bundles_formations", back_populates="formations")
