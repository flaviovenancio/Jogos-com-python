import adivinhacao
import forca

def escolha_jogo():

    print("*******************************")
    print("      escolha seu jogo         ")
    print("*******************************")

    print("(1) forca (2) adivinhação")

    jogo =int(input("Qual jogo: "))

    #vai para o jogo da forca
    if(jogo == 1):
        print("jogando forca")
        forca.jogar()

    #vai para jogo de adivinhação
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("valor inválido ")
        escolha_jogo()
if(__name__ == "__main__"):
    escolha_jogo()