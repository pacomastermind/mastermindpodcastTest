from api.database.database import SessionLocal, engine
from api.database.database import Base

from api.doc import tags_metadata

from api.esquemas.models import Categoria as CategoriaModel
from api.database.models import Categoria as CategoriaModelDB
from api.logica import categorialogica

from api.rutas.categorias import router as categoriasrutas

