import pytest
from api import engine
from sqlalchemy.exc import SQLAlchemyError,OperationalError


def test_Failconnection():
   #https://docs.sqlalchemy.org/en/20/core/exceptions.html
   with pytest.raises(SQLAlchemyError) as exconnection:
      conn=engine.connect()
   assert exconnection.type is OperationalError