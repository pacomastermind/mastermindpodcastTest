from api.database.database import SessionLocal, engine
from api.database.database import Base

from api.doc import tags_metadata

from api.esquemas.models import Autor as AutorModel
from api.esquemas.models import User as UserModel
from api.esquemas.models import AutorPodcast as AutorPodcastModel
from api.esquemas.models import Categoria as CategoriaModel
from api.esquemas.models import CategoriaCreate,UserCreate, UserResponse,Token
from api.esquemas.models import Podcast as PodcastModel
from api.esquemas.models import PodcastAutor as PodcastAutorModel
from api.esquemas.models import PodcastCreate
from api.database.models import Categoria as CategoriaModelDB
from api.database.models import Podcast as PodcastModelDB
from api.database.models import Autor as AutorModelDB
from api.database.models import User as UserModelDB

from api.logica import categorialogica,podcastlogica, autoreslogica, auth

from api.rutas.categorias import router as categoriasrutas
from api.rutas.podcasts import router as podcastsrutas
from api.rutas.autores import router as autoresrutas

