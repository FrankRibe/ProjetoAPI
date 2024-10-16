from flask import jsonify, request
from app import app, db
from app.models import Professor, Turma, Aluno

@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([professor.nome for professor in professores])

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([{"id": turma.id, "descricao": turma.descricao, "professor_id": turma.professor_id} for turma in turmas])

@app.route('/turmas', methods=['POST'])
def adicionar_turma():
    data = request.json
    if not data.get('descricao') or not data.get('professor_id'):
        return jsonify({"message": "Dados inválidos!"}), 400
    nova_turma = Turma(descricao=data['descricao'], professor_id=data['professor_id'])
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({"id": nova_turma.id, "message": "Turma adicionada com sucesso!"}), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{"id": aluno.id, "nome": aluno.nome, "idade": aluno.idade, "turma_id": aluno.turma_id} for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.json
    novo_aluno = Aluno(nome=data['nome'], idade=data['idade'], turma_id=data['turma_id'])
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"id": novo_aluno.id, "message": "Aluno adicionado com sucesso!"}), 201
