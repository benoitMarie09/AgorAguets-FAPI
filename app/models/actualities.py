from sqlalchemy import Date, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Actuality(Base):
    __tablename__ = "actualities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String, index=True)
    date = Column(Date)
    # photos