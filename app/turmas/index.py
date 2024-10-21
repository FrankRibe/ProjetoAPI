from flask import Blueprint
from .turmas_routes import turmas_blueprint

turmas = Blueprint('turmas', __name__)

turmas.add_url_rule('/turmas', 'get_turmas', turmas_blueprint.get_turmas, 
                       methods=['GET'])
turmas.add_url_rule('/turmas', 'create_turmas', turmas_blueprint.create_turmas,
                       methods=['POST'])