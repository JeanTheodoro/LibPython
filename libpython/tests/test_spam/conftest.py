import pytest

from libpython.spam.db import Conection


@pytest.fixture(scope='session')
def conection():
    conection_obj = Conection()
    yield conection_obj
    conection_obj.close()


@pytest.fixture
def session(conection):
    session_obj = conection.create_session()
    yield session_obj
    session_obj.rool_back()
    session_obj.close()
