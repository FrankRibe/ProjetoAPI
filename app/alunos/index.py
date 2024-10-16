from flask import Blueprint
from alunos_routes import get_alunos, create_aluno

alunos = Blueprint('alunos', __name__)

alunos.add_url_rule('/alunos', 'get_alunos', get_alunos,
                       methods=['GET'])
alunos.add_url_rule('/alunos', 'create_alunos', create_aluno,
                       methods=['POST'])