import unittest
from app.model_aluno_professor import dados  # Importando dados


class TestProfessores(unittest.TestCase):

    def test_lista_professores_vazia(self):
        """Testa se a lista de professores começa vazia."""
        self.assertEqual(len(dados["professores"]), 0)


if __name__ == "__main__":
    unittest.main()
