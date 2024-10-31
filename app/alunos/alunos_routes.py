from flask import (
    Blueprint, request, render_template,
    jsonify, redirect, url_for
)
from app.models import Aluno, Turma
from .alunos_model import (
    AlunoNaoEncontrado, listar_alunos, aluno_por_id,
    adicionar_aluno, atualizar_aluno, excluir_aluno
)
from datetime import datetime

alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route("/alunos", methods=["GET"])
def listar_alunos_view():
    alunos = listar_alunos()
    return render_template('aluno/alunos.html', alunos=alunos)


@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["GET"])
def exibir_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno/aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404


@alunos_blueprint.route("/aluno/novo", methods=["GET"])
def criar_aluno_view():
    return render_template('aluno/criarAlunos.html')


@alunos_blueprint.route("/alunos/<int:id_aluno>/editar", methods=["GET"])
def editar_aluno_view(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno/aluno_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({"message": "Aluno não encontrado"}), 404


@alunos_blueprint.route("/alunos", methods=["POST"])
def adicionar_aluno_view():
    data = request.form
    try:
        data_nascimento = datetime.strptime(
            data["data_nascimento"], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Data de nascimento inválida"}), 400

    if data.get("turma_id") is None:
        return jsonify({"error": "turma_id não pode ser None"}), 400

    novo_aluno = {
        "nome": data["nome"],
        "idade": data["idade"],
        "turma_id": data["turma_id"],
        "data_nascimento": data_nascimento,
        "nota_primeiro_semestre": data["nota_primeiro_semestre"],
        "nota_segundo_semestre": data["nota_segundo_semestre"],
        "media_final": data["media_final"]
    }

    try:
        adicionar_aluno(novo_aluno)
        return redirect(url_for('alunos.listar_alunos_view'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@alunos_blueprint.route("/alunos/<int:id_aluno>/atualizar",
                        methods=["GET", "POST"], endpoint="update_aluno")
def atualizar_aluno_view(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if request.method == 'POST':
        novos_dados = request.form.to_dict()
        print(f"Dados recebidos para atualização: {novos_dados}")
        try:
            atualizar_aluno(id_aluno, novos_dados)
            return redirect(url_for('listar_alunos'))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    return render_template('aluno/aluno_update.html', aluno=aluno,
                           turmas=Turma.query.all())


@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["POST"])
def excluir_aluno_view(id_aluno):
    if request.form.get('_method') == 'DELETE':
        try:
            excluir_aluno(id_aluno)
            return "", 204
        except AlunoNaoEncontrado:
            return jsonify({"message": "Aluno não encontrado"}), 404
    return jsonify({"message": "Método não permitido"}), 405
