from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import SessionLocal, engine
from api import podcastlogica, PodcastModel, PodcastCreate, PodcastAutorModel

router = APIRouter()

# Dependencia necesaria para realizar la conexion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PodcastAutorModel])
def read_podcasts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    podcasts = podcastlogica.get_podcasts(db, skip=skip, limit=limit)
    return podcasts

@router.get("/{podcast_id}", response_model=PodcastModel)
def read_categoria(podcast_id: int, db: Session = Depends(get_db)):
    podcast = podcastlogica.get_podcast(db, podcast_id=podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail="Podcast no encontrado")
    return podcast

@router.post("/", response_model=PodcastModel)
def create_podcast(podcast: PodcastCreate, db: Session = Depends(get_db)):
    return podcastlogica.create_podcast(db, podcast)