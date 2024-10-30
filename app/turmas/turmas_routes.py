from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from .turmas_model import (
    TurmaNaoEncontrado, listar_turmas, turma_por_id,
    adicionar_turma, atualizar_turma, excluir_turma
)

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
        turma = turma_por_id(id_turma)
        return render_template('turmas/turmas_id.html', turma=turma)  
    except TurmaNaoEncontrado:
        return jsonify({"message": "Turma não encontrada"}), 404

# Rota para criar uma nova turma
@turmas_blueprint.route("/turmas/novo", methods=["GET", "POST"])
def create_turma():
    if request.method == "POST":
        data = request.form

        # Converte o valor do status para booleano
        status = data.get('status') == '1'  # '1' se torna True, qualquer outra coisa se torna False
        descricao = data.get('descricao')
        professor_id = data.get('professor_id')

        try:
            # Adiciona a nova turma no banco de dados
            adicionar_turma({
                'descricao': descricao,
                'status': status,
                'professor_id': professor_id
            })
            return redirect(url_for('turmas.get_turmas'))  # Redireciona para a lista de turmas
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return render_template('turmas/criarTurmas.html')  # Renderiza o template para criar nova turma


# Rota para atualizar uma turma pelo ID
@turmas_blueprint.route("/turmas/<int:id_turma>/atualizar", methods=["GET", "POST"])
def update_turma(id_turma):
    if request.method == "POST":
        data = request.form.to_dict()  # Converte para um dicionário mutável

        # Converte o valor do status para booleano
        # Se o checkbox foi enviado, atribui True; caso contrário, atribui False
        data['status'] = 'status' in data  # O checkbox envia apenas quando está marcado

        try:
            atualizar_turma(id_turma, data)
            return redirect(url_for('turmas.get_turmas'))  # Redireciona para a lista de turmas
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
            return jsonify ({"message": "Turma não encontrada"}), 404
    return jsonify({"message": "Método não permitido."}), 405
