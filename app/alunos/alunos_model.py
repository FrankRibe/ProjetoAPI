from app import db
from app.models import Aluno


class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        return {
            "id": id_aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma": aluno.turma,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
    }
    raise AlunoNaoEncontrado

def listar_alunos():
    alunos = Aluno.query.all()
    return [
        {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma": aluno.turma,
            "data_nascimento": aluno.data_nascimento,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
    }
    for aluno in alunos
]

def adicionar_aluno(dados_aluno):
    novo_aluno = Aluno(
        nome=dados_aluno.get("nome"),
        idade=dados_aluno.get("idade"),
        turma=dados_aluno.get("turma"),
        data_nascimento=dados_aluno.get("data_nascimento"),
        nota_primeiro_semestre=dados_aluno.get("nota_primeiro_semestre"),
        nota_segundo_semestre=dados_aluno.get("nota_segundo_semestre"),
        media_final=dados_aluno("media_final")
    )

    db.session.add(novo_aluno)
    db.session.commit()

def atualizar_aluno(id_aluno, novos_dados):
    alunos = Aluno.query.get(id_aluno)
    if not alunos:
        raise AlunoNaoEncontrado
    
    nome=novos_dados.get("nome"),
    idade=novos_dados.get("idade"),
    turma=novos_dados.get("turma"),
    data_nascimento=novos_dados.get("data_nascimento"),
    nota_primeiro_semestre=novos_dados.get("nota_primeiro_semestre"),
    nota_segundo_semestre=novos_dados.get("nota_segundo_semestre"),
    media_final=novos_dados("media_final")

    db.session.commit()

def excluir_aluno(id_aluno):
    professor = Aluno.query.get(id_aluno)
    if not id_aluno:
        raise AlunoNaoEncontrado