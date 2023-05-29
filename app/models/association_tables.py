from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

bundles_formations = Table('bundles_formations', Base.metadata,
                           Column('bundle_id', ForeignKey('bundles.id'), primary_key=True),
                           Column('formation_id', ForeignKey('formations.id'), primary_key=True)
                           )
