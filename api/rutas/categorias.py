from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import SessionLocal, engine
from api import categorialogica, CategoriaModel, CategoriaCreate

router = APIRouter()

# Dependencia necesaria para realizar la conexion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CategoriaModel])
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = categorialogica.get_categorias(db, skip=skip, limit=limit)
    return categorias

@router.get("/{categoria_id}", response_model=CategoriaModel)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = categorialogica.get_categoria(db, categoria_id=categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria

@router.post("/", response_model=CategoriaModel)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return categorialogica.create_categoria(db, categoria)

@router.put("/{categoria_id}", response_model=CategoriaModel)
def update_categoria(categoria_id: int, categoria: CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = categorialogica.update_categoria(db,categoria_id,categoria)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return db_categoria
@router.delete("/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    num_delete_row = categorialogica.delete_categoria(db, categoria_id=categoria_id)
    if num_delete_row < 1:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return {"msg":"Categoría eliminada"}
