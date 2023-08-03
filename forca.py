import random

def jogar():
    #chamando as funções
    mensagem_de_apresentação()
    palavra_secreta = gera_palavra()

    #para cada letra da palavra coloca um sinal de "_"
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #inicialização do loop com a condição
    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        #verifica se a letra esta na palavra e coloca na posição certa
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1
            desenha_forca(erros)
            print("Vocẽ ainda tem {} tentaticas. ".format(7 - erros))

        enforcou = erros == 7
        #acertou é valido se nao tiver mais o sinal "_"
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Você ganhou")
    else:
        print("Você perdeu, a palavra era {} ".format(palavra_secreta))

def mensagem_de_apresentação():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def gera_palavra():
    palavras = []
    #abre o arquivo e adiciona a lista
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    #escolhe uma palavra aleatoria da lista
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
