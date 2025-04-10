import unittest
from unittest.mock import mock_open, patch  #o mock cria o arquivo fake  e  #patch acessa
from lista_palavras import ListaDePalavras
from palavra import Palavra

class TestListaDePalavras(unittest.TestCase):

    def test_carregar_arquivo_com_palavras(self):
        arquivo_fake = "gato\ncachorro\nmacaco"    

        with patch("builtins.open", mock_open(read_data=arquivo_fake)):  #abrir arquivo fake
            lista_palavras = ListaDePalavras ("arquivo_fake.txt")
        
        self.assertEqual (len(lista_palavras.palavras),3)


    def test_carregar_arquivo_sem_palavras(self):
        arquivo_fake = ""

        with patch("builtins.open", mock_open(read_data=arquivo_fake)):  #abrir arquivo fake
            lista_palavras = ListaDePalavras ("arquivo_fake.txt")
        
        self.assertEqual (len(lista_palavras.palavras),0)


    def test_escolher_palavra(self):
        arquivo_fake = "gato"

        with patch("builtins.open", mock_open(read_data=arquivo_fake)):  #abrir arquivo fake
            lista_palavras = ListaDePalavras ("arquivo_fake.txt")

        palavra = lista_palavras.escolher_palavra()
        self.assertEqual(palavra.descricao, "gato") 

    
    def test_objeto_escolher_palavra(self):  #se palavra é do tipo objeto
        arquivo_fake = "gato"

        with patch("builtins.open", mock_open(read_data=arquivo_fake)):  #abrir arquivo fake
            lista_palavras = ListaDePalavras ("arquivo_fake.txt")

        palavra = lista_palavras.escolher_palavra()
        self.assertIsInstance(palavra, Palavra)