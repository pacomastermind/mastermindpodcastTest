from sqlalchemy.orm import Session

from api import AutorModelDB, AutorModel

#Definimos la devolucion de todos los podcasts
def get_autores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AutorModelDB).offset(skip).limit(limit).all()