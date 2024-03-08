from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import SessionLocal, engine
from api import autoreslogica, AutorModelDB, AutorPodcastModel

router = APIRouter()

# Dependencia necesaria para realizar la conexion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AutorPodcastModel])
def read_podcasts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    autores = autoreslogica.get_autores(db, skip=skip, limit=limit)
    return autores