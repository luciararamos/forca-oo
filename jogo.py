from jogador import Jogador
from palavra import Palavra

class JogoDaForca:
    #atributo x tipo
    jogador: Jogador
    palavra: Palavra
    letras_escolhidas: set = set()
    tentativas = 6
    palavra_atual: str
    acertou_palavra= False
    letras_acertadas= set()

    def __init__(self, jogador, palavra):    #jogador inicia o jogo sorteando a palavra
        self.jogador = jogador
        self.palavra = palavra
        self.letras_escolhidas = set()
        self.letras_acertadas = set()
        self.acertou_palavra = False
        self.palavra_atual = ["_" for _ in self.palavra.descricao]
        

    def exibir_palavra_oculta(self):  #exibir a palavra ocultada
        return " ".join("_" for _ in self.palavra.descricao)
    

    def atualizar_palavra_atual(self): #atualizar palavra atual
        self.palavra_atual = ""
        for letra in self.palavra.descricao:
            if letra in self.letras_acertadas:
                self.palavra_atual+=letra
            else :
                self.palavra_atual+="_"

    def verificar_fim_de_jogo(self):           #definir vitoria
        if "_" not in self.palavra_atual:
            print(f"Parabéns, {self.jogador.nome}! Você acertou a palavra: {self.palavra}")
            return True
        
        if self.tentativas == 0:               #definir derrota
            print(f"Você perdeu! A palavra era: {self.palavra}")
            return True
        return False


    def processar_tentativa(self, letra):     #letra já foi escolhida
        if letra in self.letras_escolhidas:
            print("Você já escolheu essa letra.")
            return
        else: 
            self.letras_escolhidas.add(letra) 
        
        if letra in self.palavra.descricao:  #letra encontrada
            print("Você acertou!")
            self.letras_acertadas.add(letra)
        else:                            #tentativas restantes
            self.tentativas -= 1
            print(f"Letra incorreta. Você tem {self.tentativas} tentativas restantes.")

        self.exibir_palavra_oculta()
        self.verificar_fim_de_jogo()

