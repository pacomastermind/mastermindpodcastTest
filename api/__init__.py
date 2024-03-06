from api.database.database import SessionLocal, engine
from api.database.database import Base

from api.doc import tags_metadata

from api.esquemas.models import Categoria as CategoriaModel
from api.esquemas.models import CategoriaCreate
from api.esquemas.models import Podcast as PodcastModel
from api.esquemas.models import PodcastCreate
from api.database.models import Categoria as CategoriaModelDB
from api.database.models import Podcast as PodcastModelDB
from api.logica import categorialogica,podcastlogica

from api.rutas.categorias import router as categoriasrutas
from api.rutas.podcasts import router as podcastsrutas

