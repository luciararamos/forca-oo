import unittest
from palavra import Palavra

class TestPalavra(unittest.TestCase):
    def setUp(self):
        self.palavra = Palavra("anel")
        
    def test_init(self):
        self.assertEqual(self.palavra.descricao,"anel")
    
    def test_str(self):
        self.assertEqual(str(self.palavra), "anel")
        self.assertEqual(str(self.palavra), self.palavra.descricao)

