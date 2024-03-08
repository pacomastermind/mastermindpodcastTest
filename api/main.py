from fastapi import FastAPI,Depends
from api import SessionLocal,engine
from api import tags_metadata, categoriasrutas, podcastsrutas, autoresrutas
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

# Objeto app de tipo FastApi
app = FastAPI(
    title="Mastermind Podcast API",
    description="ApiRestFul para la gestión de los podcast realizados por Mastermind",
    version="0.1",
    contact={
        "name":"Paco Gómez",
        "url":"http://www.mastermind.ac"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)
oauth2_scheme = OAuth2PasswordBearer("/token")

@app.get("/")
async def root():
    return {"info": "Bienvenido a MastermindPodcast"}

@app.get("/users/me")
async def usuario(token: str = Depends(oauth2_scheme)):
    print(token)
    return {"info": "Usuario actual"}

@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
    print(form_data.username,form_data.password)
    return {"access_token":"Pakito","token_type":"bearer"}

#CATEGORIAS
app.include_router(
    categoriasrutas,
    tags=["categorias"],
    prefix="/categorias",
)

#PODCASTS
app.include_router(
    podcastsrutas,
    tags=["podcasts"],
    prefix="/podcasts",
)

#AUTORES
app.include_router(
    autoresrutas,
    tags=["autores"],
    prefix="/autores",
)

