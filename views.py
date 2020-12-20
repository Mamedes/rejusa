from flask import Flask
"""Extensão Flask"""


def init_app(app: Flask):
    """ Inicialização de extensões"""

    @app.route('/')
    def index():
        return '<h1>Hello World!<h1>'

    @app.route('/contato')
    def contato():
        return '<h1>Meu Contato!<h1>'
