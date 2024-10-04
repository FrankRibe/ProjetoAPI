from flask import render_template
from app import app, db
from app.models import Professor, Turma, Aluno

@app.route('/')
def index():
    return "<h1>Bem-vindo à Escola API!</h1>"

@app.route('/professores')
def listar_professores():
    professores = Professor.query.all()
    return {"professores": [prof.nome for prof in professores]}

@app.route('/turmas')
def listar_turmas():
    turmas = Turma.query.all()
    return {"turmas": [turma.descricao for turma in turmas]}

@app.route('/alunos')
def listar_alunos():
    alunos = Aluno.query.all()
    return {"alunos": [aluno.nome for aluno in alunos]}