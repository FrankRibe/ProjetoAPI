from flask import Blueprint
from .alunos_routes import alunos_blueprint

# Criação do blueprint para as rotas de alunos
alunos = Blueprint('alunos', __name__)

# Adicionando as rotas usando o blueprint de alunos
alunos.add_url_rule('/alunos', 'get_alunos', alunos_blueprint.get_alunos, methods=['GET'])
alunos.add_url_rule('/alunos', 'create_alunos', alunos_blueprint.create_aluno, methods=['POST'])
alunos.add_url_rule('/alunos/<int:id_aluno>', 'get_aluno', alunos_blueprint.get_aluno, methods=['GET'])
alunos.add_url_rule('/alunos/<int:id_aluno>', 'update_aluno', alunos_blueprint.update_aluno, methods=['PUT'])
alunos.add_url_rule('/alunos/<int:id_aluno>', 'delete_aluno', alunos_blueprint.delete_aluno, methods=['DELETE'])