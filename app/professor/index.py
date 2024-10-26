from flask import Blueprint
from .professor_routes import (
    get_professores, create_professor, update_professor,
    delete_professor, get_professores_id
)

professor = Blueprint('professores', __name__)

# Aqui você registra as rotas
professor.add_url_rule('/professores', 'get_professores', get_professores,
                       methods=['GET'])
professor.add_url_rule('/professores/<int:id_professor>', 'get_professores_id',
                       get_professores_id, methods=['GET'])
professor.add_url_rule('/professores', 'create_professor', create_professor,
                       methods=['POST'])
professor.add_url_rule('/professores/<int:id_professor>',
                       'update_professor', update_professor,
                       methods=['PUT'])
professor.add_url_rule('/professores/<int:id_professor>',
                       'delete_professor', delete_professor,
                       methods=['DELETE'])
