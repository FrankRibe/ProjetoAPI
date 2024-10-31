import unittest
from app.model_aluno_professor import Aluno


class TestAluno(unittest.TestCase):

    def test_criar_aluno(self):
        aluno = Aluno(nome="Carlos", idade=20)
        self.assertEqual(aluno.nome, "Carlos")
        self.assertEqual(aluno.idade, 20)

    def test_atualizar_idade(self):
        aluno = Aluno(nome="Ana", idade=18)
        aluno.idade = 21
        self.assertEqual(aluno.idade, 21)

    def test_nome_completo(self):
        aluno = Aluno(nome="João Silva", idade=22)
        self.assertIn("João", aluno.nome)
        self.assertIn("Silva", aluno.nome)


if __name__ == '__main__':
    unittest.main()
