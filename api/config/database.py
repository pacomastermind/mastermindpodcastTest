from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Conexion a la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/mastermindpodcast'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

#Debug
#comprobamos la correcta conexion
with engine.connect() as connection:
    result = connection.execute(text("select nombre from categorias"))
    for row in result:
        print("nombre:", row.nombre)

#Creamos la sesión de trabajo
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)