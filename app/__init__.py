from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados (ajuste conforme necessário)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instância do banco de dados
db = SQLAlchemy(app)

# Importando as rotas e modelos
from app import routes, models