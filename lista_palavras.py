class ListaDePalavras:   #sortear palavra da lista presente no arquivo txt

    def __init__(self, arquivo="palavras_forca.txt"):
        self.arquivo = arquivo
        self.palavras = self.carregar_palavras()

    def carregar_palavras(self):
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f.readlines()]
        
    def escolher_palavra(self):
        import random
        return random.choice(self.palavras)