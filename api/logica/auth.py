from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Annotated, Union
from decouple import config

from api import UserModelDB, UserModel
#Creamos un podcast
def create_user(db: Session,  user: UserModel):
    db_User =UserModelDB(**user.dict())
    db.add(db_User)
    db.commit()
    db.refresh(db_User)
    return db_User

def get_user(db: Session, username: str):
    return db.query(UserModelDB).filter(UserModelDB.username == username).first()

def authenticate_user(db: Session, username: str, password: str, pwd_context ):
    user = get_user(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config("SECRET_KEY"), algorithm=config("ALGORITHM"))
    return encoded_jwt
