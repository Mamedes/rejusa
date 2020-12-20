from sqlalchemy import Column, Integer, Sequence, ForeignKey, String, Numeric
from DB.db_connector import DBConnector
from DB.model.base_model import BaseModel


class Debito(BaseModel, DBConnector.get_base_model()):
    """
    Classe de debitos.
    """
    __tablename__ = 'debitos'
    id = Column(Integer, Sequence('id_debito'), primary_key=True)
    id_credores = Column(Integer, ForeignKey('credores.id'), nullable=False)
    descricao = Column(String(200), nullable=False)
    valor = Column(Numeric, nullable=False)

    def __init__(self):
        super().__init__()