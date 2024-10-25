from flask import Blueprint
from .turmas_routes import (
    get_turmas, create_turma, update_turma,
    delete_turma, get_turma
)

# Criação do blueprint para as rotas de turmas
turmas = Blueprint('turmas', __name__)

# Adicionando as rotas usando o blueprint de turmas
turmas.add_url_rule('/turmas', 'get_turmas',
                    get_turmas, methods=['GET'])
turmas.add_url_rule('/turmas', 'create_turmas',
                    create_turma, methods=['POST'])
turmas.add_url_rule('/turmas/<int:id_turma>', 'get_turmas',
                    get_turma, methods=['GET'])
turmas.add_url_rule('/turmas/<int:id_turma>', 'update_turmas',
                    update_turma, methods=['PUT'])
turmas.add_url_rule('/turmas/<int:id_turma>', 'delete_turmas',
                    delete_turma, methods=['DELETE'])
