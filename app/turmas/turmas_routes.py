from flask import Blueprint, request, jsonify
from .turmas_model import TurmaNaoEncontrado, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

alunos_blueprint = Blueprint('turmas', __name__)

# Rota para listar todas as turmas
@alunos_blueprint.route("/turmas", methods=["GET"])
def get_turmas():
    return jsonify(listar_turmas())

# Rota para obter uma turma pelo ID
@alunos_blueprint.route("/turmas/<int:id_turma>", methods=["GET"])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except TurmaNaoEncontrado:
        return jsonify({"message": "Turma não encontrado"}), 404

# Rota para criar uma nova turma
@alunos_blueprint.route("/turmas", methods=["POST"])
def create_turma():
    data = request.json
    try:
        adicionar_turma(data)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Rota para atualizar uma turma pelo ID
@alunos_blueprint.route("/turmas/<int:id_turma>", methods=["PUT"])
def update_turma(id_turma):
    data = request.json
    try:
        atualizar_turma(id_turma, data)
        return jsonify(turma_por_id(id_turma))
    except TurmaNaoEncontrado:
        return jsonify({"message": "Turma não encontrado"}), 404

# Rota para excluir uma turma pelo ID
@alunos_blueprint.route("/turmas/<int:id_turma>", methods=["DELETE"])
def delete_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return "", 204
    except TurmaNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404