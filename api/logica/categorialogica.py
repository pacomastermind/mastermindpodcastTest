from sqlalchemy.orm import Session

from api import CategoriaModelDB

#Definimos la devolucion de todas las categorias
def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoriaModelDB).offset(skip).limit(limit).all()
