from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from animelist import settings

DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    return create_engine(URL(**settings.DATABASE))

def creat_items_table(engine:Engine):
    DeclarativeBase.metadata.create_all(engine)

class Items(DeclarativeBase):
    __tablename__ = 'Animes'

    Titulo = Column('Titulo', String, primary_key=True)
    Nota = Column('Nota', Integer)
    Eps = Column('Epsodios', Integer)
    Ano = Column('Ano', Integer)
    Membros = Column('Membros', Integer)
    Assista = Column('Assista', String, primary_key=True)