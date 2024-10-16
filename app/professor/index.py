from flask import Blueprint
from professor_routes import get_professores, create_professor

professor = Blueprint('professores', __name__)

# Aqui você registra as rotas
professor.add_url_rule('/professores', 'get_professores', get_professores,
                       methods=['GET'])
professor.add_url_rule('/professores', 'create_professor', create_professor,
                       methods=['POST'])
