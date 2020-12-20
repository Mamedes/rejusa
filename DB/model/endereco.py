from sqlalchemy import Column, Sequence, String,Integer, SmallInteger, ForeignKey, BigInteger
from Model.BaseModel import *
from DB.DBConnector import *


class Endereco(BaseModel, DBConnector.get_base_model()):
    """
    Classe de endereços
    """
    __tablename__ = 'enderecos'
    id = Column(BigInteger, Sequence('id_endereco'), primary_key=True)
    id_recuperanda = Column(Integer, ForeignKey('recuperandas.id'), nullable=False)
    logradouro = Column(String(200), nullable=False)
    complemento = Column(String(200))
    bairro = Column(String(100))
    cep = Column(String(10), nullable=False)
    id_municipio = Column(SmallInteger, ForeignKey('municipios.id'), nullable=False)

    def __init__(self):
        super().__init__()
