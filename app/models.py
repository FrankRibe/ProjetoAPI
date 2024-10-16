from flask_sqlalchemy import SQLAlchemy
from app import db

#db = SQLAlchemy()

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(50))
    observacoes = db.Column(db.Text)

    # Relacionamento com Turma
    turmas = db.relationship('Turma', backref='professor', lazy=True)


class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    # Relacionamento com Professor
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    # Relacionamento com Alunos
    alunos = db.relationship('Aluno', backref='turma', lazy="select")


class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    # Relacionamento com Turma
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
