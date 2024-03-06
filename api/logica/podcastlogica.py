from sqlalchemy.orm import Session

from api import PodcastModelDB, PodcastModel

#Definimos la devolucion de todos los podcasts
def get_podcasts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PodcastModelDB).offset(skip).limit(limit).all()

#Devolucion de un podcast por id
def get_podcast(db: Session, podcast_id: int):
    return db.query(PodcastModelDB).filter(PodcastModelDB.id == podcast_id).first()

#Creamos un podcast
def create_podcast(db: Session,  podcast: PodcastModel):
    db_Podcast =PodcastModelDB(**podcast.dict())
    db.add(db_Podcast)
    db.commit()
    db.refresh(db_Podcast)
    return db_Podcast
#Actualizamos categoria
#def update_categoria(db: Session, categoria_id: int, categoria: CategoriaCreate):
#    db_Categoria = db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).first()
#    if(db_Categoria):
#        db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).update(categoria.dict())
#        db.commit()
#        db.refresh(db_Categoria)
#    return db_Categoria
#Eliminamos una categoria
#def delete_categoria(db: Session, categoria_id: int):
#    num_rows =db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).delete()
#    if(num_rows>0):
#        db.commit()
#    return num_rows
