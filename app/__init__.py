import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True

# Configuração do banco de dados (ajuste conforme necessário)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instância do banco de dados
db = SQLAlchemy(app)

# Importando as rotas e modelos
from .routes import *
from .models import *