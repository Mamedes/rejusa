from sqlalchemy import Column, Integer, String, DateTime, Sequence

from DB.db_connector import DBConnector
from DB.model.base_model import BaseModel


class Usuario(BaseModel, DBConnector.get_base_model()):

    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('id_usuario'), primary_key=True)
    login = Column(String(30), unique=True, nullable=False)
    senha = Column(String(32), nullable=False)
    ultimo_acesso = Column(DateTime)

    def __init__(self):
        super().__init__()


