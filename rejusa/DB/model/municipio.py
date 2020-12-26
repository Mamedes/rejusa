from sqlalchemy import Column, Sequence, String, SmallInteger, ForeignKey
from rejusa.DB.db_connector import DBConnector
from rejusa.DB.model.base_model import BaseModel


class Municipio(BaseModel, DBConnector.get_base_model()):
    """
    Classe de municípios
    """
    __tablename__ = 'municipios'
    id = Column(SmallInteger, Sequence('id_municipio'), primary_key=True)
    id_estado = Column(SmallInteger, ForeignKey('estados.id'), nullable=False)
    nome = Column(String(50))

    def __init__(self):
        super().__init__()



