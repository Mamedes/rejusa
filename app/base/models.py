from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Sequence, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app import db, login_manager
from app.base.util import hash_pass


class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None


class Grupo(db.Model):
    """
    Classe de Grupo.
    """
    __tablename__ = 'grupos'
    id = Column(Integer, Sequence('id_grupo'), primary_key=True)
    nome = Column(String(200), nullable=False, unique=True)
    recuperanda = relationship('Recuperanda', backref='grupo')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.nome)


class Recuperanda(db.Model):

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

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.nome_fantasia)


class Credor(db.Model):
    """
    Classe de credores.
    """
    __tablename__ = 'credores'
    id = Column(Integer, Sequence('id_credor'), primary_key=True)
    id_recuperanda = Column(Integer, ForeignKey('recuperandas.id'), nullable=False)
    nome = Column(String(200), nullable=False)
    cnpj = Column(String(18), nullable=False)
    telefone = Column(String(14))
    email = Column(String(100), nullable=False)
    debitos = relationship('Debito', backref='credor')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.nome)


class Debito(db.Model):
    """
    Classe de debitos.
    """
    __tablename__ = 'debitos'
    id = Column(Integer, Sequence('id_debito'), primary_key=True)
    id_credores = Column(Integer, ForeignKey('credores.id'), nullable=False)
    descricao = Column(String(200), nullable=False)
    valor = Column(Numeric, nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.descricao)
