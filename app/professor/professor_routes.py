from flask import (
    Blueprint, request, render_template,
    jsonify, redirect, url_for
)
from app.models import Professor
from app.professor.professor_model import (
    ProfessorNaoEncontrado, listar_professores, professor_por_id,
    adicionar_professor, atualizar_professor, excluir_professor
)

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route("/professor", methods=["GET"])
def listar_professores_view():
    professores = listar_professores()
    return render_template('professor/professor.html', professores=professores)

@professores_blueprint.route("/professor/<int:id_professor>", methods=["GET"])
def exibir_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor/professor_id.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route("/professores/novo", methods=["GET"])
def criar_professor_view():
    return render_template('professor/criarProfessor.html')

@professores_blueprint.route("/professor/<int:id_professor>/editar", methods=["GET"])
def editar_professor_view(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor/professor_update.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route("/professores", methods=["POST"])
def adicionar_professor_view():
    data = request.form

    # Criação do novo professor com os dados do formulário
    novo_professor = {
        "nome": data["nome"],
        "idade": data["idade"],
        "materia": data["materia"],
        "observacoes": data.get("observacoes", "")  # Captura observações, se fornecidas
    }

    try:
        # Chamada para a função que adiciona o professor ao banco de dados
        adicionar_professor(novo_professor)
        return redirect(url_for('professores.listar_professores_view'))  # Redireciona para a lista de professores
    except Exception as e:
        # Em caso de erro, você pode tratar a exceção e retornar uma mensagem apropriada
        return jsonify({"error": str(e)}), 400  # Retorna um erro 400 (Bad Request)


@professores_blueprint.route("/professores/<int:id_professor>/atualizar", methods=["GET", "POST"])
def atualizar_professor_view(id_professor):
    try:
        professor = professor_por_id(id_professor)
        if request.method == "POST":
            novos_dados = request.form.to_dict()
            atualizar_professor(id_professor, novos_dados)
            return redirect(url_for('professores.listar_professores_view'))
        return render_template('professor/professor_update.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route("/professores/<int:id_professor>", methods=["POST"])
def excluir_professor_view(id_professor):
    if request.form.get ("_method") == "DELETE":
        try:
            excluir_professor(id_professor)
            return "", 204
        except ProfessorNaoEncontrado:
            return jsonify ({"message": "Professor não encontrado"}), 404
    return jsonify ({"message": "Método não permitido"}), 405    