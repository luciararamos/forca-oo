class JogoDaForca:

    def __init__(self, jogador, lista_de_palavras):    #jogador inicia o jogo sorteando a palavra
        self.jogador = jogador
        self.palavra = lista_de_palavras.escolher_palavra()
        self.tentativas = 6
        self.letras_escolhidas = set()
        self.palavra_atual = ["_" for _ in self.palavra]

    def exibir_palavra_oculta(self):  #exibir a palavra ocultada
        print(" ")

    def processar_tentativa(self, letra):     #letra já foi escolhida
        if letra in self.letras_escolhidas:
            print("Você já escolheu essa letra.")
            return
        else: 
            self.letras_escolhidas.add(letra) 
        
        if letra in self.palavra:  #letra encontrada
            print("Você acertou!")
     
        else:                            #tentativas restantes
            self.tentativas -= 1
            print(f"Letra incorreta. Você tem {self.tentativas} tentativas restantes.")

        self.exibir_palavra_oculta()

    def verificar_fim_de_jogo(self):           #definir vitoria
        if "_" not in self.palavra_atual:
            print(f"Parabéns, {self.jogador.nome}! Você acertou a palavra: {self.palavra}")
            return True
        
        if self.tentativas == 0:               #definir derrota
            print(f"Você perdeu! A palavra era: {self.palavra}")
            return True
        return False