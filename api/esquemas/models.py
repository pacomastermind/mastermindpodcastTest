from typing import Union
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class CategoriaCreate(BaseModel):
    nombre: str

