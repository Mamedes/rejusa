from sqlalchemy import Column, Sequence, String, SmallInteger
from sqlalchemy.orm import relationship
from Model.BaseModel import *
from DB.DBConnector import *


class Estado(BaseModel, DBConnector.base):
    """
    Classe de estados
    """
    __tablename__ = 'estados'
    id = Column(SmallInteger, Sequence('id_estado'), primary_key=True)
    nome = Column(String(30), nullable=False)
    uf = Column(String(2), nullable=False)
    municipios = relationship('Municipio', backref='estado')

    def __init__(self):
        super().__init__()

