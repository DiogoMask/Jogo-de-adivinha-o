import random

#Inicio do jogo
print("*******************************")
print("Bem vindo ao jogo de advinhação!")
print("*******************************")
#Varíaveis iniciais para começar o jogo/sem elas decladas antes, o jogo não inicia
total_de_tentativas = 0
pontos = 1000

#Definição da dificuldade, qunto mais dificil menos tentativas
print("Qual nivel de dificuldade você quer?")
print("Facíl(1) Médio(2) Difícil(3)")

nível= int(input("Defina o nível: "))

if (nível == 1):
    total_de_tentativas = 20
elif (nível == 2):
    total_de_tentativas = 10
elif (nível == 3 ):
    total_de_tentativas = 5

#Bonus de diversidade, quis fazer uma graça no projeto para torna-lo diferente

#Aqui o jogador define se quer diversificar seu jogo, fazendo o jogo aconter com apenas numeros pares ou impares
diversidade = int(input("Quer diversidade no jogo? digite 1 para sim e 0 para não: "))

#If's para fazer essa modalidade do jogo acontecer
if (diversidade==1): 
        #se o jogador digitar 1, o programa pede para que ele escolha a modadalidade par ou impar:
        parimpar = int(input("Apenas Numeros ímpares (digite 1) Apenas numeros pares (digite 2): "))
        #O sistema recolhe o numero fornecido pelo jogador, e usa o mesmo para fazer o calculo no numero secreto
        numero_secreto= random.randrange(0, 101, parimpar)
#Agora se o jogador quiser jogar o jogo padrão é só digitar 0 :D
if (diversidade==0):
        numero_secreto= random.randrange(0, 101)
        
 # para rodadas de 1 até numero de tentativas (+1 pq o número final de uma range nunca conta)....
for rodada in range(1, total_de_tentativas + 1):
    #...O Sistema pede um chute para o jogador! 
    chute = int(input("Qual número o Pc esta pensando?(chute um número de 1 a 100) "))
    #Agora o sistema te mostra qual numero foi digitado...
    print("voce digitou:", chute)
    #...e em qual tentativa você se encontra
    print(f"tentativa {rodada} de {total_de_tentativas}")
    #aqui vai um controle para que não haja numeros gigantescos, que o sistema avisa o jogador sobre!
    if (chute < 1 or chute >100):
        print("Você deve chutar um numero entre 1 e 100!!!")
        continue
        

    #variaveis para o sistema calcular se..
    #...voce acertou, ou seja, numero_secreto for igual ao chute...
    acertou = numero_secreto == chute
    #variaveis para saber se o seu chute é maior ou menor que o numero secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    print("*"* 35)
    #Se você acerta o numero, o sistema identifica, notifica que você acertou, e te mostra a pontuação!
    if (acertou):
        print(f"você acertou e fez {pontos} pontos!!!!")
        break
    #caso você não acerte o sistema te da dicas, como, se seu chute fo maior que o numero, ou menor!
    else:
        if (chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif (chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto")
        #calculo dos pontos
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("*"* 35)
#Fim de jogo, e a revelação do numero secreto
print(f"Fim do jogo o numero secreto era: {numero_secreto}")

