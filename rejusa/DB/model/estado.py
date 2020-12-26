from sqlalchemy import Column, Sequence, String, SmallInteger
from sqlalchemy.orm import relationship
from rejusa.DB.db_connector import DBConnector
from rejusa.DB.model.base_model import BaseModel


class Estado(BaseModel, DBConnector.get_base_model()):
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

