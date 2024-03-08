#Incorporar definiciones de classes futuras
from __future__ import annotations

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Table
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


#https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many
podcast_autor = Table(
    "podcast_autor",
    Base.metadata,
    Column("podcast_id", ForeignKey("podcasts.id"), primary_key=True),
    Column("autor_id", ForeignKey("autores.id"), primary_key=True),
)


class Podcast(Base):

    __tablename__ = "podcasts"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    url = Column(String)
    # Annotated example
    # categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    # categoria: Mapped["Categoria"] = relationship(back_populates="podcasts")
    # Non-Annotated example
    categoria_id = mapped_column(ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="podcasts")
    autores: Mapped[List[Autor]] = relationship(
        secondary=podcast_autor, back_populates="podcasts"
    )
class Autor(Base):

    __tablename__ = "autores"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    nacionalidad = Column(String)
    podcasts: Mapped[List[Podcast]] = relationship(
        secondary=podcast_autor, back_populates="autores"
    )

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    nombre = Column(String)
    activo = Column(Boolean)





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