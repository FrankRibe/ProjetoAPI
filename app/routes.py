from flask import render_template, request, jsonify
from app import app, db
from app.models import Professor, Turma, Aluno


@app.route('/')
def index():
    return "<h1>Bem-vindo à Escola API!</h1>"


@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return {
        "professores": [
            {
                "id": prof.id,
                "nome": prof.nome,
                "idade": prof.idade,
                "materia": prof.materia,
                "observacoes": prof.observacoes
            }
            for prof in professores
        ]
    }


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


@app.route('/turmas')
def listar_turmas():
    turmas = Turma.query.all()
    return {"turmas": [turma.descricao for turma in turmas]}


@app.route('/alunos')
def listar_alunos():
    alunos = Aluno.query.all()
    return {"alunos": [aluno.nome for aluno in alunos]}
