from flask import Flask
from dotenv import load_dotenv
from rejusa.DB.model.credores import Credor
from rejusa.DB.model.debito import Debito
from rejusa.DB.model.endereco import Endereco
from rejusa.DB.model.estado import Estado
from rejusa.DB.model.grupo import Grupo
from rejusa.DB.model.municipio import Municipio
from rejusa.DB.model.recuperanda import Recuperanda
from rejusa.DB.model.usuario import Usuario
from rejusa.admin import admin


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
    app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
    app.config['SECRET_KEY'] = 'mysecret'
    load_dotenv()
    init_database()
    admin.init_app(app)
    return app



