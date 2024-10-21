from flask import render_template, jsonify, request
from datetime import datetime
from . import app, db
from app.models import Professor, Turma, Aluno


@app.route("/")
def index():
    return "<h1>Bem-vindo à Escola API!</h1>"

@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify({
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
    })

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([
        {
            "id": turma.id,
            "descricao": turma.descricao,
            "professor_id": turma.professor_id
        }
        for turma in turmas
    ])

@app.route('/turmas', methods=['POST'])
def adicionar_turma():
    data = request.json
    if not data.get('descricao') or not data.get('professor_id'):
        return jsonify({"message": "Dados inválidos!"}), 400
    nova_turma = Turma(descricao=data['descricao'], professor_id=data['professor_id'])
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({
        "id": nova_turma.id,
        "message": "Turma adicionada com sucesso!"
    }), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return  {
        "alunos":[
            {
                "id": aluno.id,
                "nome": aluno.nome,
                "idade": aluno.idade,
                "turma_id": aluno.turma_id,
                "data_nascimento": aluno.data_nascimento,
                "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
                "nota_segundo_semestre": aluno.nota_segundo_semestre,
                "media_final": aluno.media_final
            }
            for aluno in alunos
        ]
    }

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.json

    data_nascimento = datetime.strptime(data["data_nascimento"], '%Y-%m-%d').date()

    novo_aluno = Aluno(
        nome=data["nome"],
        idade=data["idade"],
        turma_id=data["turma_id"],
        data_nascimento=data_nascimento,  
        nota_primeiro_semestre=data["nota_primeiro_semestre"],
        nota_segundo_semestre=data["nota_segundo_semestre"],
        media_final=data["media_final"]
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({
        "id": novo_aluno.id,
        "message": "Aluno adicionado com sucesso!"
    }), 201
