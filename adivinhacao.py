import random

def jogar():

    print("*******************************")
    print("Bem vindo ao jogo de advinhacao")
    print("*******************************")
    #gera o numero secreto a função randrange() recebe 2 argumentos, o valor inicial e o valor final
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000


    print("Qual o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Díficil ")

    nivel = int(input("Defina o nível: "))
    # seleciona o nivel de dificuldade
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    #laço que incrementa as tentativas de acordo com o nivel
    for rodada in range (1, total_de_tentativas +1):
        print("Tentativa {} de {} ".format(rodada,total_de_tentativas))

        chute_dig = input("Digite um número entre 1 e 100 : ")
        print("O numero digitado foi: ", chute_dig)
        #converte para um inteiro
        chute = int(chute_dig)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100 ")
            continue

        acertou  =  chute  == numero_secreto
        maior    =  chute  >  numero_secreto
        menor    =  chute  <  numero_secreto

        #condições que compara os valores digitados
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, o seu numero é maior que o numero secreto")
            elif (menor):
                print("Você errou, o seu numero é menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("o numero secreto era {} ".format(numero_secreto))
    print("Fim de jogo")


if(__name__ == "__main__"):
    jogar()
