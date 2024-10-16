from flask import Blueprint, request, jsonify
from .alunos_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno

alunos_blueprint = Blueprint('alunos', __name__)

# Rota para listar todos os alunos
@alunos_blueprint.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(listar_alunos())

# Rota para obter um aluno pelo ID
@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["GET"])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404

# Rota para criar um novo aluno
@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.json
    try:
        adicionar_aluno(data)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Rota para atualizar um aluno pelo ID
@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["PUT"])
def update_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404

# Rota para excluir um aluno pelo ID
@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return "", 204
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404
