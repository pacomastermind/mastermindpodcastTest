from fastapi import FastAPI
from api import SessionLocal,engine

from api import tags_metadata, categoriasrutas

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

@app.get("/")
async def root():
    return {"info": "Bienvenido a MastermindPodcast"}

#CATEGORIAS
app.include_router(
    categoriasrutas,
    tags=["categorias"],
    prefix="/categorias",
)

