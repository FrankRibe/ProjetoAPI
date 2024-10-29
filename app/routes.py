from flask import (
    render_template, jsonify, request, redirect, url_for, flash
)
from app import app, db
from app.models import Professor, Turma, Aluno


@app.route("/")
def index():
    professores = Professor.query.all()
    turmas = Turma.query.all()
    alunos = Aluno.query.all()
    return render_template('index.html', professores=professores,
                           turmas=turmas, alunos=alunos)


@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return render_template('professor/professores.html',
                           professores=professores)


@app.route('/professores', methods=['POST'])
def adicionar_professor():
    data = request.get_json()
    novo_professor = Professor(
        nome=data['nome'], idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes', "")
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({"message": "Professor adicionado com sucesso!"}), 201


@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = Professor.query.get(id)
    if professor is None:
        return jsonify({"error": "Professor não encontrado"}), 404

    dados = request.get_json()
    professor.nome = dados.get('nome', professor.nome)
    professor.idade = dados.get('idade', professor.idade)
    professor.materia = dados.get('materia', professor.materia)
    professor.observacoes = dados.get('observacoes', professor.observacoes)

    db.session.commit()
    return jsonify({"mensagem": "Professor atualizado com sucesso!"}), 200


@app.route('/professores/<int:id>', methods=['DELETE'])
def excluir_professor(id):
    professor = Professor.query.get(id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return jsonify({"message": "Professor excluído com sucesso!"}), 200
    return jsonify({"message": "Professor não encontrado!"}), 404


@app.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return render_template('turma/turmas.html', turmas=turmas)


@app.route('/turmas', methods=['POST'])
def adicionar_turma():
    data = request.json
    if not data.get('descricao') or not data.get('professor_id'):
        return jsonify({"message": "Dados inválidos!"}), 400
    nova_turma = Turma(
        descricao=data['descricao'], professor_id=data['professor_id'])
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({
        "id": nova_turma.id,
        "message": "Turma adicionada com sucesso!"
    }), 201


# Rota para listar alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template('aluno/alunos.html', alunos=alunos)

# Rota para adicionar aluno (GET)


@app.route('/alunos/adicionar', methods=['GET'])
def adicionar_aluno_form():
    return render_template('aluno/criarAlunos.html')

# Rota para adicionar aluno (POST)


@app.route('/alunos/adicionar', methods=['POST'])
def adicionar_aluno():
    data = request.form
    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        # Preencha outros campos conforme necessário
    )
    db.session.add(novo_aluno)
    db.session.commit()
    flash('Aluno adicionado com sucesso!', 'success')
    return redirect(url_for('listar_alunos'))
