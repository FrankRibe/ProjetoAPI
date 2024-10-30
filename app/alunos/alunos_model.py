from datetime import datetime
from app import db
from app.models import Aluno, Turma


class AlunoNaoEncontrado(Exception):
    pass


def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        return {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma": aluno.turma_id,
            "data_nascimento": aluno.data_nascimento.strftime('%Y-%m-%d'),
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
            "turma": aluno.turma_id,
            "data_nascimento": aluno.data_nascimento.strftime('%Y-%m-%d'),
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
        }
        for aluno in alunos
    ]


def adicionar_aluno(dados_aluno):
    try:
        print(f"Dados recebidos: {dados_aluno}")  # Para ver os dados recebidos
        # Corrigido para usar 'turma_id'
        turma_id = dados_aluno.get("turma_id")
        # Para verificar se o ID da turma está correto
        print(f"ID da turma: {turma_id}")

        if turma_id is None:
            raise ValueError("turma_id não pode ser None")

        turma = Turma.query.get(turma_id)
        if turma is None:
            raise ValueError(f"Turma com id {turma_id} não existe.")

        # Verifica se data_nascimento é uma string, se não, não converte
        if isinstance(dados_aluno.get("data_nascimento"), str):
            data_nascimento = datetime.strptime(
                dados_aluno.get("data_nascimento"), '%Y-%m-%d').date()
        else:
            # Assume que já é um objeto date
            data_nascimento = dados_aluno.get("data_nascimento")

        # Criação do novo aluno
        novo_aluno = Aluno(
            nome=dados_aluno.get("nome"),
            idade=dados_aluno.get("idade"),
            turma_id=turma_id,  # Passando o ID da turma
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=dados_aluno.get("nota_primeiro_semestre"),
            nota_segundo_semestre=dados_aluno.get("nota_segundo_semestre"),
            media_final=dados_aluno.get("media_final")
        )

        db.session.add(novo_aluno)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback em caso de erro
        print(f"Ocorreu um erro ao adicionar aluno: {e}")  # Para depuração
        raise e  # Relevante para que você possa ver o erro


def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado

    print(f"Novos dados para o aluno {id_aluno}: {novos_dados}")  # Para depuração

    aluno.nome = novos_dados.get("nome")
    aluno.idade = novos_dados.get("idade")

    # Corrigido para garantir que turma_id não seja None
    turma_id = novos_dados.get("turma_id")
    if turma_id is None:
        raise ValueError("turma_id é obrigatório!")
    aluno.turma_id = turma_id

    # Verifica e converte a data de nascimento
    if isinstance(novos_dados.get("data_nascimento"), str):
        aluno.data_nascimento = datetime.strptime(
            novos_dados.get("data_nascimento"), '%Y-%m-%d').date()
    else:
        aluno.data_nascimento = novos_dados.get(
            "data_nascimento")  # Assume que já é um objeto date

    aluno.nota_primeiro_semestre = novos_dados.get("nota_primeiro_semestre")
    aluno.nota_segundo_semestre = novos_dados.get("nota_segundo_semestre")
    aluno.media_final = novos_dados.get("media_final")

    db.session.commit()


def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
