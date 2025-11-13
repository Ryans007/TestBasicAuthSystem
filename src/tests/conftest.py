import sys
import os

# Adiciona a pasta src ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from index import app
from database_ import AuthBase, get_users_db


# CRIA BANCO DE TESTE EM MEMÓRIA
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


# Override da dependência DB
@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def override_get_db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

app.dependency_overrides[get_users_db] = override_get_db


# Cliente para requisições
@pytest.fixture
def client():
    # 1. Cria as tabelas ANTES de cada teste
    AuthBase.metadata.create_all(bind=engine)

    # 2. Usa 'with' para rodar o teste
    with TestClient(app) as c:
        yield c

    # 3. Destrói as tabelas DEPOIS de cada teste
    AuthBase.metadata.drop_all(bind=engine)
