import unittest
from jogador import Jogador

class TestJogador(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador("Luciara", 27)
        
    def test_nome_do_jogador(self):
        self.assertEqual(self.jogador.nome, "Luciara")

    def test_idade_do_jogador(self):
        self.assertEqual(self.jogador.idade, 27)
