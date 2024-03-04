from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api import Base

class Categoria(Base):

    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)