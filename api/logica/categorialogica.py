from sqlalchemy.orm import Session

from api import CategoriaModelDB,CategoriaModel, CategoriaCreate

#Definimos la devolucion de todas las categorias
def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoriaModelDB).offset(skip).limit(limit).all()

#Devolucion de una categoria por id
def get_categoria(db: Session, categoria_id: int):
    return db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).first()

#Creamos una categoria
def create_categoria(db: Session,  categoria: CategoriaModel):
    db_Categoria =CategoriaModelDB(**categoria.dict())
    db.add(db_Categoria)
    db.commit()
    db.refresh(db_Categoria)
    return db_Categoria
#Actualizamos categoria
def update_categoria(db: Session, categoria_id: int, categoria: CategoriaCreate):
    db_Categoria = db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).first()
    if(db_Categoria):
        db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).update(categoria.dict())
        db.commit()
        db.refresh(db_Categoria)
    return db_Categoria
#Eliminamos una categoria
def delete_categoria(db: Session, categoria_id: int):
    num_rows =db.query(CategoriaModelDB).filter(CategoriaModelDB.id == categoria_id).delete()
    if(num_rows>0):
        db.commit()
    return num_rows
