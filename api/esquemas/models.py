from typing import Union
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class CategoriaCreate(BaseModel):
    nombre: str

class PodcastBase(BaseModel):
    id: int
    titulo: str
    descripcion: str
    url: str

class Podcast(PodcastBase):
    autor_id: int
    categoria_id: int
    categoria : Categoria
    class Config:
        orm_mode = True

class PodcastCreate(BaseModel):
    titulo: str
    descripcion: str
    url: str
    autor_id: int
    categoria_id: int