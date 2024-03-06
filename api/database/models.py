from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from api import Base

class Categoria(Base):

    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    #https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many
    #Annotated example
    #podcasts: Mapped[List["Podcast"]] = relationship()
    # Non-Annotated example
    podcasts = relationship("Podcast", back_populates="categoria")

class Podcast(Base):

    __tablename__ = "podcasts"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    url = Column(String)
    autor_id = Column(Integer)
    # Annotated example
    # categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    # categoria: Mapped["Categoria"] = relationship(back_populates="podcasts")
    # Non-Annotated example
    categoria_id = mapped_column(ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="podcasts")


#class Episodio(Base):

    #    __tablename__ = "episodios"

    #    id = Column(Integer, primary_key=True)
    #    numepisodio = Column(Integer)
    #    numtemporada  = Column(Integer)
    #    titulo = Column(String)
    #    descripcion = Column(String)
    #    url = Column(String)
    #    duracion = Column(Integer)
    #    fechacreacion= Column(Date)
    #    podcast_id = Column(Integer, ForeignKey("podcasts.id"))

#    owner = relationship("Podcast", back_populates="episodios")