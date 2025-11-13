from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

AUTH_DB_URL = "sqlite:///./database_/users.db"
auth_engine = create_engine(AUTH_DB_URL, connect_args={"check_same_thread": False})
auth_session = sessionmaker(autocommit=False, autoflush=False, bind=auth_engine)
AuthBase = declarative_base()

def get_users_db():
    """
    Gera uma sessão de banco de dados para o banco de usuários.

    Yields:
        Session: Sessão do banco de dados.
    """
    db = auth_session()
    try:
        yield db
    finally:
        db.close()