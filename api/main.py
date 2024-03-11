from fastapi import FastAPI,Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from api import SessionLocal,engine
from api import tags_metadata, categoriasrutas, podcastsrutas, autoresrutas
from api import UserCreate,auth, UserResponse, Token
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from decouple import config

from fastapi.middleware.cors import CORSMiddleware

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

origins = [
    "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
oauth2_scheme = OAuth2PasswordBearer("/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/")
async def root():
    return {"info": "Bienvenido a MastermindPodcast"}

@app.get("/users/me")
async def usuario(token: str = Depends(oauth2_scheme)):
    print(token)
    return {"info": "Usuario actual"}

@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    print("Username ${form_data.username}")
    user = auth.authenticate_user(db, form_data.username, form_data.password,pwd_context)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(config("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.post("/user/signup", response_model=UserResponse)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    user.password=pwd_context.hash(user.password)
    return auth.create_user(db,user)


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

