import unittest
from app.model_aluno_professor import (
    adiciona_aluno,
    aluno_por_id,
    AlunoNaoEncontrado,
    lista_alunos,
    apaga_tudo  # Importando a função
)


class TestAlunos(unittest.TestCase):

    def setUp(self):
        # Limpa a lista de alunos antes de cada teste
        apaga_tudo()
        # Adiciona um aluno para os testes
        self.aluno = {"nome": "lucas", "id": 15}
        adiciona_aluno(self.aluno)

    def test_adiciona_aluno(self):
        """Testa se o aluno é adicionado corretamente."""
        self.assertIn(self.aluno, lista_alunos())

    def test_aluno_por_id(self):
        """Testa a recuperação do aluno por ID."""
        aluno = aluno_por_id(15)
        self.assertEqual(aluno['nome'], "lucas")

    def test_aluno_nao_encontrado(self):
        """Testa a exceção quando o aluno não é encontrado."""
        with self.assertRaises(AlunoNaoEncontrado):
            aluno_por_id(999)  # ID que não existe


if __name__ == "__main__":
    unittest.main()
