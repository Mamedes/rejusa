from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm, CreateGrupoForm
from app.base.models import User, Grupo
from app.base.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


@blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    create_grupo_form = CreateGrupoForm(request.form)
    result = Grupo.query.filter_by()
    if result:
        return render_template('dashboard/dashboard.html',
                               grupos=result, form=create_grupo_form)
    else:
        return render_template('dashboard/dashboard.html',
                               msg='Não encontramaos grupos cadastrados na nossa base',
                               success=False, form=create_grupo_form)


@blueprint.route('grupo_add', methods=['GET', 'POST'])
@login_required
def grupo_add():
    create_grupo_form = CreateGrupoForm(request.form)
    if 'grupo' in request.form:

        grupo = request.form['grupo']
        print(grupo)
        # Check grupo exists
        grupo = Grupo.query.filter_by(nome=grupo).first()
        if grupo:
            return render_template('dashboard/dashboard.html',
                                   msg='Grupo já registrado',
                                   success=False,
                                   form=create_grupo_form)
        # else we can create the user
        grupo = Grupo(**request.form)
        db.session.add(grupo)
        db.session.commit()

        return redirect(url_for('base_blueprint.dashboard'))

    else:
        return redirect(url_for('base_blueprint.dashboard'))
# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
