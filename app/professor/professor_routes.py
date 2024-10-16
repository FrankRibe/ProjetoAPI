from flask import Blueprint, request, jsonify
from professor_model import (
    ProfessorNaoEncontrado, listar_professores, professor_por_id,
    adicionar_professor, atualizar_professor, excluir_professor
)


professores_blueprint = Blueprint('professores', __name__)


@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(listar_professores())


@professores_blueprint.route('/professores/<int:id_professor>',
                             methods=['GET'])
def set_professores(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Requisição inválida. "
                        "Esperado JSON com dados do professor."}), 400
    
    required_keys = {"nome", "idade", "materia"}
    if not required_keys.issubset(data.keys()):
        return jsonify({"error": f"Dados incompletos. Campos {required_keys}"
                        " são necessários."}), 400
    adicionar_professor(data)
    return jsonify(data), 201


@professores_blueprint.route('/professores/<int:id_professor>',
                             methods=['PUT'])
def update_professor(id_professor):
    data = request.json
    try:
        atualizar_professor(id_professor, data)
        return jsonify(professor_por_id(id_professor))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/<int:id_professor>',
                             methods=['DELETE'])
def delete_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return '', 204
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
