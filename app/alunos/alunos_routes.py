from flask import Blueprint, request, jsonify
from .alunos_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno
from datetime import datetime

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(listar_alunos())

@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["GET"])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno) 
        return jsonify(aluno) 
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404  

@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.json
    
    # Converter a string de data_nascimento para um objeto date
    try:
        data_nascimento = datetime.strptime(data["data_nascimento"], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Data de nascimento inválida"}), 400

    # Certifique-se de que a turma_id não é None antes de adicionar o aluno
    if data.get("turma_id") is None:
        return jsonify({"error": "turma_id não pode ser None"}), 400

    novo_aluno = {
        "nome": data["nome"],
        "idade": data["idade"],
        "turma_id": data["turma_id"],
        "data_nascimento": data_nascimento,  # Use o objeto date aqui
        "nota_primeiro_semestre": data["nota_primeiro_semestre"],
        "nota_segundo_semestre": data["nota_segundo_semestre"],
        "media_final": data["media_final"]
    }

    try:
        adicionar_aluno(novo_aluno)  # Chame a função adicionar_aluno com o novo aluno
        return jsonify(novo_aluno), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["PUT"])
def update_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404

@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return "", 204
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404
