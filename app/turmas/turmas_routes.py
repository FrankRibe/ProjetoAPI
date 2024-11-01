from sqlalchemy.orm import joinedload
from flask import (
    Blueprint, request, render_template,
    redirect, url_for, jsonify
)
from .turmas_model import (
    TurmaNaoEncontrado, listar_turmas, turma_por_id,
    adicionar_turma, atualizar_turma, excluir_turma
)
from app.models import Turma

turmas_blueprint = Blueprint('turmas', __name__)

# Rota para listar todas as turmas


@turmas_blueprint.route("/turmas", methods=["GET"])
def get_turmas():
    turmas = listar_turmas()
    return render_template('turmas/turmas.html', turmas=turmas)

# Rota para obter uma turma pelo ID


@turmas_blueprint.route("/turmas/<int:id_turma>", methods=["GET"])
def get_turma(id_turma):

    try:
        turma = Turma.query.options(joinedload(
            Turma.professor)).filter_by(id=id_turma).first()
        if not turma:
            raise TurmaNaoEncontrado
        return render_template('turmas/turmas_id.html', turma=turma)
    except TurmaNaoEncontrado:
        return jsonify({"message": "Turma não encontrada"}), 404

# Rota para criar uma nova turma


@turmas_blueprint.route("/turmas/novo", methods=["GET", "POST"])
def create_turma():
    if request.method == "POST":
        data = request.form

        # Converte o valor do status para booleano
        # '1' se torna True, qualquer outra coisa se torna False
        status = data.get('status') == '1'
        descricao = data.get('descricao')
        professor_id = data.get('professor_id')

        try:
            # Adiciona a nova turma no banco de dados
            adicionar_turma({
                'descricao': descricao,
                'status': status,
                'professor_id': professor_id
            })
            # Redireciona para a lista de turmas
            return redirect(url_for('turmas.get_turmas'))
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    # Renderiza o template para criar nova turma
    return render_template('turmas/criarTurmas.html')


# Rota para atualizar uma turma pelo ID
@turmas_blueprint.route("/turmas/<int:id_turma>/atualizar", methods=["GET", "POST"])
def update_turma(id_turma):
    if request.method == "POST":
        data = request.form.to_dict()  # Converte para um dicionário mutável

        # Converte o valor do status para booleano
        # Se o checkbox foi enviado, atribui True; caso contrário, atribui False
        # O checkbox envia apenas quando está marcado
        data['status'] = 'status' in data

        try:
            atualizar_turma(id_turma, data)
            # Redireciona para a lista de turmas
            return redirect(url_for('turmas.get_turmas'))
        except TurmaNaoEncontrado:
            return jsonify({"message": "Turma não encontrada"}), 404

    try:
        turma = turma_por_id(id_turma)
        return render_template('turmas/turmas_update.html', turma=turma)
    except TurmaNaoEncontrado:
        return jsonify({"message": "Turma não encontrada"}), 404


# Rota para excluir uma turma pelo ID
@turmas_blueprint.route("/turmas/<int:id_turma>", methods=["POST"])
def excluir_turma_view(id_turma):
    if request.form.get("_method") == "DELETE":
        try:
            excluir_turma(id_turma)
            return "", 204
        except TurmaNaoEncontrado:
            return jsonify({"message": "Turma não encontrada"}), 404
    return jsonify({"message": "Método não permitido."}), 405
