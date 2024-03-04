from fastapi import FastAPI
from api import SessionLocal,engine

app = FastAPI()

@app.get("/")
async def root():
    return {"info": "Bienvenido a MastermindPodcast"}

