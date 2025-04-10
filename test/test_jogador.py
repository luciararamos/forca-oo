import unittest
from jogador import Jogador

class TestJogador(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador("Luciara", 27)
        
    def test_init(self):
        self.assertEqual([self.jogador.nome, self.jogador.idade],["Luciara", 27])
    
