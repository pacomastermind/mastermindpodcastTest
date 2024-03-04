from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from api import SessionLocal, engine
from api import categorialogica, CategoriaModel

router = APIRouter()

# Dependencia necesaria para realizar la conexion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CategoriaModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = categorialogica.get_categorias(db, skip=skip, limit=limit)
    return categorias
