import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


class DBConnector:
    """
    Classe de conexão ao banco de dados e criação de sessões.
    """
    __sessionmaker = None
    __engine = None
    __base = None

    def __init__(self):
        pass

    @classmethod
    @contextmanager
    def get_session(cls) -> Session:
        """
        Retorna uma sessão com o banco de dados gerenciada pelo contexto
        """
        if DBConnector.__sessionmaker is None:
            DBConnector.config()
        session = DBConnector.__sessionmaker()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise ModelException(str(e))
        finally:
            session.close()

    @classmethod
    def get_engine(cls) -> Engine:
        """
        Retorna a engine de conexão ao banco de dados.
        """
        if DBConnector.__engine is None:
            DBConnector.config()
        return DBConnector.__engine

    @classmethod
    def get_base_model(cls) -> object:
        """
        Retorna a BaseModel para instanciamento de models de base declarativa.
        """
        if DBConnector.__base is None:
            DBConnector.__base = declarative_base()
        return DBConnector.__base

    @classmethod
    def config(cls) -> None:
        """
        Configura o banco de dados.
        Precisa ser chamado apenas uma vez.
        """
        url = f"{os.environ.get('DB_ENGINE')}://"\
              f"{os.environ.get('DB_USER')}:"\
              f"{os.environ.get('DB_PASS')}@"\
              f"{os.environ.get('DB_SERVER')}:"\
              f"{os.environ.get('DB_PORT')}/"\
              f"{os.environ.get('DB_NAME')}"
        DBConnector.__engine = create_engine(url)
        DBConnector.__sessionmaker = sessionmaker(DBConnector.__engine, expire_on_commit=False)


class ModelException(Exception):
    """
    Exceção do módulo de Modelos
    """
    def __init__(self, message):
        self.message = message
