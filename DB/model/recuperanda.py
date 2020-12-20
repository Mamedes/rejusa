from sqlalchemy import Column, Integer, String, DateTime, Sequence, or_
from sqlalchemy.orm import relationship
from Model.BaseModel import *
from DB.DBConnector import *


class Recuperanda(BaseModel, DBConnector.base):

    __tablename__ = 'recuperandas'
    id = Column(Integer, Sequence('id_recuperanda'), primary_key=True)
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    cnpj = Column(String(18), nullable=False)
    ie = Column(String(100), nullable=False)
    porte = Column(String(100), nullable=False)
    responsavel = Column(String(100), nullable=False)
    telefone = Column(String(14))
    email = Column(String(100), nullable=False)
    avatar = Column(String(100), nullable=False)
    observacao = Column(String(100), nullable=False)
    grupo = relationship("Grupo", back_populates="recuperanda")

    def __init__(self):
        super().__init__()


