from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criação da instância do Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {
        "timeout": 30  # Espera por 30 segundos antes de retornar erro de banco de dados bloqueado
    }
}


# Instância do banco de dados
db = SQLAlchemy(app)

# Importando o blueprint após a instância do app ter sido criada
from app.turmas.turmas_routes import turmas_blueprint  # Caminho correto para o blueprint
app.register_blueprint(turmas_blueprint)
 
from app.alunos.alunos_routes import alunos_blueprint
app.register_blueprint(alunos_blueprint)


# Importando modelos e rotas
from app import models, routes  # Certifique-se de que as rotas estão definidas

