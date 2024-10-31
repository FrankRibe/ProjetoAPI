import unittest
from app.model_aluno_professor import Professor


class TestProfessor(unittest.TestCase):

    def test_criar_professor(self):
        professor = Professor(nome="Dra. Julia", disciplina="Matemática")
        self.assertEqual(professor.nome, "Dra. Julia")
        self.assertEqual(professor.disciplina, "Matemática")

    def test_alterar_disciplina(self):
        professor = Professor(nome="Dr. Carlos", disciplina="História")
        professor.disciplina = "Geografia"
        self.assertEqual(professor.disciplina, "Geografia")

    def test_nome_professor(self):
        professor = Professor(nome="Prof. Souza", disciplina="Ciências")
        self.assertTrue(professor.nome.startswith("Prof."))


if __name__ == '__main__':
    unittest.main()
