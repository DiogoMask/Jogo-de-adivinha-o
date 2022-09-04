import advinhacao
import forca

print("*******************************")
print("*******Escolha seu jogo********")
print("*******************************")

print("(1)Forca (2)advinhacao")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("Voce escolheu forca!")
    forca.jogar()
elif jogo == 2:
    print("Voce escolheu advinhacao!")
    advinhacao.jogar()