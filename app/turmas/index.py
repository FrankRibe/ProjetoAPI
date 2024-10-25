from flask import Blueprint
from.turmas_routes import turmas_blueprint

# Criação do blueprint para as rotas de turmas
turmas = Blueprint('turmas', __name__)

# Adicionando as rotas usando o blueprint de turmas
turmas.add_url_rule('/turmas', 'get_turmas', turmas_blueprint.get_turmas, methods=['GET'])
turmas.add_url_rule('/turmas', 'create_turmas', turmas_blueprint.create_turmas, methods=['POST'])
turmas.add_url_rule('/turmas/<int:id_turmas>', 'get_turmas', turmas_blueprint.get_turmas, methods=['GET'])
turmas.add_url_rule('/turmas/<int:id_turmas>', 'update_turmas', turmas_blueprint.update_turmas, methods=['PUT'])
turmas.add_url_rule('/turmas/<int:id_turmas>', 'delete_turmas', turmas_blueprint.delete_turmas, methods=['DELETE'])