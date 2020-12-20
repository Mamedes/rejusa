from sqlalchemy import Column, Integer, Sequence, ForeignKey, String, Boolean, BigInteger
from sqlalchemy.orm import relationship
from Model.BaseModel import *
from DB.DBConnector import *


class Credor(BaseModel, DBConnector.base):
    """
    Classe de credores.
    """
    __tablename__ = 'credores'
    id = Column(Integer, Sequence('id_credor'), primary_key=True)
    id_recuperanda = Column(BigInteger, ForeignKey('recuperandas.id'), nullable=False)
    nome = Column(String(200), nullable=False)
    cnpj = Column(String(18), nullable=False)
    telefone = Column(String(14))
    email = Column(String(100), nullable=False)
    debitos = relationship('Debito', backref='credor')

    def __init__(self):
        super().__init__()
