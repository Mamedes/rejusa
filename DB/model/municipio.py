from sqlalchemy import Column, Sequence, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from Model.BaseModel import *
from DB.DBConnector import *


class Municipio(BaseModel, DBConnector.base):
    """
    Classe de municípios
    """
    __tablename__ = 'municipios'
    id = Column(SmallInteger, Sequence('id_municipio'), primary_key=True)
    id_estado = Column(SmallInteger, ForeignKey('estados.id'), nullable=False)
    nome = Column(String(50))
    enderecos = relationship('Endereco', backref='municipio')

    def __init__(self):
        super().__init__()



