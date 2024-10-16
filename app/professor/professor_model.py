from app import db
from app.models import Professor


class ProfessorNaoEncontrado(Exception):
    pass


def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if professor:
        return {
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "matéria": professor.materia,
            "observações": professor.observacoes
        }
    raise ProfessorNaoEncontrado


def listar_professores():
    professores = Professor.query.all()
    return [
        {
            "id": professor.id,
            "nome": professor.nome,
            "idade": professor.idade,
            "matéria": professor.materia,
            "observações": professor.observacoes
        }
        for professor in professores
    ]


def adicionar_professor(dados_professor):
    novo_professor = Professor(
        nome=dados_professor.get("nome"),
        idade=dados_professor.get("idade"),
        materia=dados_professor.get("materia"),
        observacoes=dados_professor.get("observacoes", "")
    )
    db.session.add(novo_professor)
    db.session.commit()


def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado

    professor.nome = novos_dados.get("nome", professor.nome)
    professor.idade = novos_dados.get("idade", professor.idade)
    professor.materia = novos_dados.get("materia", professor.materia)
    professor.observacoes = novos_dados.get("observacoes",
                                            professor.observacoes)

    db.session.commit()


def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado

    db.session.delete(professor)
    db.session.commit()
