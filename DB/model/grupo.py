from sqlalchemy import Column, Integer, Sequence, ForeignKey, String, Boolean, BigInteger
from sqlalchemy.orm import relationship
from Model.BaseModel import *
from DB.DBConnector import *


class Grupo(BaseModel, DBConnector.base):
    """
    Classe de grupos.
    """
    __tablename__ = 'grupos'
    id = Column(Integer, Sequence('id_grupo'), primary_key=True)
    nome = Column(String(200), nullable=False)
    recuperanda = relationship("Recuperanda", uselist=False, back_populates="grupos")
    def __init__(self):
        super().__init__()

