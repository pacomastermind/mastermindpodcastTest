from api.database.database import SessionLocal, engine
from api.database.database import Base

from api.doc import tags_metadata

from api.esquemas.models import Autor as AutorModel
from api.esquemas.models import AutorPodcast as AutorPodcastModel
from api.esquemas.models import Categoria as CategoriaModel
from api.esquemas.models import CategoriaCreate
from api.esquemas.models import Podcast as PodcastModel
from api.esquemas.models import PodcastAutor as PodcastAutorModel
from api.esquemas.models import PodcastCreate
from api.database.models import Categoria as CategoriaModelDB
from api.database.models import Podcast as PodcastModelDB
from api.database.models import Autor as AutorModelDB
from api.logica import categorialogica,podcastlogica, autoreslogica

from api.rutas.categorias import router as categoriasrutas
from api.rutas.podcasts import router as podcastsrutas
from api.rutas.autores import router as autoresrutas

