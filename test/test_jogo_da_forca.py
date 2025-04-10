import unittest
from jogador import Jogador
from palavra import Palavra
from jogo import JogoDaForca  

class TesteJogoDaForca(unittest.TestCase):  #testes baseado na palavra anel

    def setUp(self):
        self.jogador = Jogador("Luciara", 27)
        self.palavra = Palavra("anel")
        self.jogo = JogoDaForca(self.jogador, self.palavra)

    def test_init(self):
        self.assertEqual(self.jogo.tentativas, 6)
        self.assertEqual(self.jogo.letras_escolhidas, set())
        self.assertEqual(self.jogo.letras_acertadas, set())  
        self.assertFalse(self.jogo.acertou_palavra)
        self.assertEqual(self.jogo.palavra_atual, ["_"] * len(self.palavra.descricao))
        
    def test_exibir_palavra_oculta(self):
        resultado = self.jogo.exibir_palavra_oculta()
        self.assertEqual(resultado, "_ _ _ _")  

    def test_processar_tentativa_correta(self):
        self.jogo.processar_tentativa("n")
        self.assertIn("n", self.jogo.letras_acertadas)
        self.assertEqual(self.jogo.tentativas, 6)

    def test_processar_tentativa_errada(self):
        tentativas_antes = self.jogo.tentativas
        self.jogo.processar_tentativa("z")
        self.assertNotIn("z", self.jogo.letras_acertadas)
        self.assertEqual(self.jogo.tentativas, tentativas_antes - 1)

    def test_tentativa_repetida(self):
        self.jogo.processar_tentativa("n")
        tentativas_antes = self.jogo.tentativas
        self.jogo.processar_tentativa("n")
        self.assertEqual(self.jogo.tentativas, tentativas_antes)

    def test_vitoria(self):
        self.jogo.letras_acertadas = set("anel")
        self.jogo.atualizar_palavra_atual()
        fim_de_jogo = self.jogo.verificar_fim_de_jogo()
        self.assertTrue(fim_de_jogo)

    def test_derrota(self):
        self.jogo.tentativas = 0
        fim_de_jogo = self.jogo.verificar_fim_de_jogo()
        self.assertTrue(fim_de_jogo)

