from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from DB.db_connector import DBConnector
from DB.model.credores import Credor
from DB.model.debito import Debito
from DB.model.endereco import Endereco
from DB.model.estado import Estado
from DB.model.grupo import Grupo
from DB.model.municipio import Municipio
from DB.model.recuperanda import Recuperanda
from DB.model.usuario import Usuario

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
