from jogo import JogoDaForca
from lista_palavras import ListaDePalavras
from jogador import Jogador

def criar_jogador():
    nome= input("Digite seu nome:")
    idade= int(input("Digite sua idade:"))
    return Jogador(nome, idade)

def jogar(jogador):

    lista_palavras= ListaDePalavras()
    palavra= lista_palavras.escolher_palavra()
    jogo_da_forca= JogoDaForca(jogador=jogador, palavra=palavra)

    print(f"A palavra sorteada possui {len(jogo_da_forca.palavra.descricao)} letras.")
    jogo_da_forca.atualizar_palavra_atual()
    print(" ".join(jogo_da_forca.palavra_atual))
    
    while jogo_da_forca.tentativas > 0 and not jogo_da_forca.acertou_palavra: #enquanto tiver erros restantes e não acertar a palavra
        letra = input("Digite uma letra:")
        jogo_da_forca.processar_tentativa(letra=letra)

        jogo_da_forca.atualizar_palavra_atual()     #mostra a nova versão da palavra
        print(" ".join(jogo_da_forca.palavra_atual))
        
        if "_" not in jogo_da_forca.palavra_atual:
            print("Você ganhou!")
            jogo_da_forca.acertou_palavra = True

    if not jogo_da_forca.acertou_palavra:
            print(f"Você perdeu! A palavra era '{jogo_da_forca.palavra}'.")

jogador = None

while True:
    print("Escolha sua ação")
    print("1 - Criar jogador")
    print("2 - Jogar")
    acao= int(input())


    if acao == 1:
        jogador = criar_jogador()
        print(jogador)
        jogar(jogador)

    elif acao == 2:
        if jogador is None:
            print("Você precisa criar um jogador antes de jogar.")
        else:
            jogar(jogador)
