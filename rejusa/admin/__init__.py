from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from rejusa.DB.db_connector import DBConnector
from rejusa.DB.model.credores import Credor
from rejusa.DB.model.debito import Debito
from rejusa.DB.model.endereco import Endereco
from rejusa.DB.model.estado import Estado
from rejusa.DB.model.grupo import Grupo
from rejusa.DB.model.municipio import Municipio
from rejusa.DB.model.recuperanda import Recuperanda
from rejusa.DB.model.usuario import Usuario

admin = Admin()


def init_app(app):

    admin.name = "Rejusa"
    admin.template_mode = "bootstrap4"
    admin.init_app(app)
    with DBConnector.get_session() as session:
        admin.add_view(ModelView(Grupo, session))
        admin.add_view(ModelView(Recuperanda, session))
        admin.add_view(ModelView(Endereco, session))
        admin.add_view(ModelView(Credor, session))
        admin.add_view(ModelView(Debito, session))
        admin.add_view(ModelView(Municipio, session))
        admin.add_view(ModelView(Estado, session))
        admin.add_view(ModelView(Usuario, session))
