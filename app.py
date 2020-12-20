import views
from flask import Flask
from dotenv import load_dotenv

from DB.model.credores import Credor
from DB.model.debito import Debito
from DB.model.endereco import Endereco
from DB.model.estado import Estado
from DB.model.grupo import Grupo
from DB.model.municipio import Municipio
from DB.model.recuperanda import Recuperanda
from DB.model.usuario import Usuario


def init_database():
    Credor()
    Debito()
    Endereco()
    Estado()
    Grupo()
    Municipio()
    Recuperanda()
    Usuario()


def create_app():
    """Factory principoal"""
    app = Flask(__name__)
    load_dotenv()
    init_database()
    views.init_app(app)
    return app



