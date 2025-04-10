import unittest
from unittest.mock import mock_open, patch  #o mock cria o arquivo fake  e  #patch acessa
from lista_palavras import ListaDePalavras

class TestListaDePalavras(unittest.TestCase):

    def test_carregar_palavras_com_arquivo_fake(self):
        arquivo_fake = "gato\ncachorro\nmacaco"    

        with patch("builtins.open", mock_open(read_data=arquivo_fake)):  #abrir arquivo fake
            self.assertEqual(len(lista.palavras), 3)

