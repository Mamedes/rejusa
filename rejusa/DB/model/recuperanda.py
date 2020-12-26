from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from rejusa.DB.db_connector import DBConnector
from rejusa.DB.model.base_model import BaseModel


class Recuperanda(BaseModel, DBConnector.get_base_model()):

    __tablename__ = 'recuperandas'
    id = Column(Integer, Sequence('id_recuperanda'), primary_key=True)
    id_grupo = Column(Integer, ForeignKey('grupos.id'), nullable=False)
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


    def __init__(self):
        super().__init__()


