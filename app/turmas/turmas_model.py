from app import db
from app.models import Turma, Professor

class TurmaNaoEncontrado(Exception):
    pass

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if turma:
        return {
            "id": id_turma.id,
            "descricao": turma.descricao,
            "professor": turma.professor,
            "status": turma.status
    }
    raise TurmaNaoEncontrado

def listar_turmas():
    turmas = Turma.query.all()
    return [
        {
            "id": turma.id,
            "descricao": turma.descricao,
            "professor": turma.professor_id,
            "status": turma.status
    }
    for turma in turmas
]

def adicionar_turma(dados_turma):
    novo_turma = Turma(
        descricao=dados_turma.get("descricao"),
        professor=dados_turma.get("professor"),
        status=dados_turma.get("status"),
    )

    db.session.add(novo_turma)
    db.session.commit()

def atualizar_turma(id_turma, novos_dados):
    turmas = Turma.query.get(id_turma)
    if not turmas:
        raise TurmaNaoEncontrado
    
    descricao=novos_dados.get("descricao"),
    professor=novos_dados.get("professor"),
    status=novos_dados.get("status"),

    db.session.commit()

def excluir_turma(id_turma):
    professor = Turma.query.get(id_turma)
    if not id_turma:
        raise TurmaNaoEncontrado