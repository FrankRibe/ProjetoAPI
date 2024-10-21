from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configuração do banco de dados (ajuste conforme necessário)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {
        "timeout": 30
    }
}

# Instância do banco de dados
db = SQLAlchemy(app)

from app.professor.professor_routes import professores_blueprint
app.register_blueprint(professores_blueprint)

# Importando as rotas e modelos
from app import routes, models
