from sqlalchemy import Column, Integer, Sequence,  String
from sqlalchemy.orm import relationship
from DB.db_connector import DBConnector
from DB.model.base_model import BaseModel


class Grupo(BaseModel, DBConnector.get_base_model()):
    """
    Classe de grupos.
    """
    __tablename__ = 'grupos'
    id = Column(Integer, Sequence('id_grupo'), primary_key=True)
    nome = Column(String(200), nullable=False)
    recuperanda = relationship('Recuperanda', backref='grupo')

    def __init__(self):
        super().__init__()

