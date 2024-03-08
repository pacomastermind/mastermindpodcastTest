#Incorporar definiciones de classes futuras
from __future__ import annotations

from typing import Union
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class CategoriaCreate(BaseModel):
    nombre: str

class Autor(BaseModel):
    id: int
    nombre: str
    nacionalidad: str
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    nombre: str
    activo: bool

class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    password: str
    class Config:
        orm_mode = True

class UserResponse(UserBase):
    id: int
class Token(BaseModel):
    access_token: str
    token_type: str

#Prevenir loops
class AutorPodcast(Autor):
    podcasts : list[Podcast]

class PodcastBase(BaseModel):
    id: int
    titulo: str
    descripcion: str
    url: str

class Podcast(PodcastBase):
    categoria_id: int
    categoria : Categoria
    class Config:
        orm_mode = True

class PodcastAutor(Podcast):
    autores : list[Autor]
    class Config:
        orm_mode = True

class PodcastCreate(BaseModel):
    titulo: str
    descripcion: str
    url: str
    categoria_id: int