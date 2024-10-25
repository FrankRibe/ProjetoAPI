from app import db
from app.models import Turma, Professor


class TurmaNaoEncontrado(Exception):
    pass


def turma_por_id(id_turma):
    # print(f"Turma com ID: {id_turma}")
    turma = Turma.query.get(id_turma)
    if turma:
        # print("Turma encontrada:", turma)
        return {
            "id": turma.id,
            "descricao": turma.descricao,
            "professor": turma.professor_id,
            "status": turma.status
        }
    # print("Turma não encontrada")
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
    try:
        print(f"Dados Recebidos: {dados_turma}")
        professor_id = dados_turma.get("professor_id")
        print(f"ID do Professor: {professor_id}")

        if professor_id is None:
            raise ValueError("professor_id não pode ser None")

        professor = Professor.query.get(professor_id)
        if professor is None:
            raise ValueError(f"Professor com id `{professor_id}` não existe")

        nova_turma = Turma(
            descricao=dados_turma.get("descricao"),
            professor_id=professor_id,
            status=dados_turma.get("status")
        )

        db.session.add(nova_turma)
        db.session.commit()

    except Exception as e:
        print(f"Erro ao adicionar turma: {e}")
        raise


def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrado

    turma.descricao = novos_dados.get("descricao")
    turma.professor_id = novos_dados.get("professor_id")
    turma.status = novos_dados.get("status")

    db.session.commit()


def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrado

    db.session.delete(turma)
    db.session.commit()
