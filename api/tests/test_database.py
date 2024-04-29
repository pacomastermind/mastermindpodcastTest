import pytest
from api import engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def test_connection():
    try:
        engine.connect()
        with engine.connect() as connection:
            result = connection.execute(text("select nombre from categorias"))
            rows = result.all()
        assert len(rows) > 0
    except SQLAlchemyError as excinfo:
        pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")