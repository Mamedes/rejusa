from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, DataRequired


# login and registration

class LoginForm(FlaskForm):
    """"
    Create Grupo Form
    """
    username = StringField('Username', id='username_login', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    """"
    Create Grupo Form
    """
    username = StringField('Username', id='username_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create', validators=[DataRequired()])


class CreateGrupoForm(FlaskForm):
    """"
    Create Grupo Form
    """
    nome = StringField('Nome', id='nome_create', validators=[DataRequired()])


class CreateRecuperandaForm(FlaskForm):
    """"
    Create Recuperandas Form
    """
    id_grupo = IntegerField('ID Grupo', id='id_grupo_create', validators=[DataRequired()])
    razao_social = StringField('Razão Social', id='razao_social_create', validators=[DataRequired()])
    nome_fantasia = StringField('Nome Fantasia', id='nome_fantazia_create', validators=[DataRequired()])
    cnpj = StringField('CNPJ', id='cnpj_create', validators=[DataRequired()])
    ie = StringField('IE', id='ie_create', validators=[DataRequired()])
    porte = StringField('Porte', id='porte_create', validators=[DataRequired()])
    responsavel = StringField('Responsavel', id='responsavel_create', validators=[DataRequired()])
    telefone = StringField('Telefone', id='telefone_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired()])
    avatar = StringField('Avatar', id='avatar_create', validators=[DataRequired()])
    observacao = StringField('Observacao', id='nome_create', validators=[DataRequired()])


class CreateCredorForm(FlaskForm):
    """"
    Create Recuperandas Form
    """
    id_recuperanda = IntegerField('ID Recuperanda', id='id_recuperanda_create', validators=[DataRequired()])
    nome = StringField('Nome', id='nome_create', validators=[DataRequired()])
    cnpj = StringField('CNPJ', id='cnpj_create', validators=[DataRequired()])
    telefone = StringField('Telefone', id='telefone_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired()])


class CreateDebitoForm(FlaskForm):
    """"
    Create Debito Form
    """
    id_credores = IntegerField('ID Credores', id='id_credores_create', validators=[DataRequired()])
    descricao = StringField('Descrição', id='descricao_create', validators=[DataRequired()])
    valor = StringField('Valor', id='valor_create', validators=[DataRequired()])



