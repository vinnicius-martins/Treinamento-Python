from random import randrange
escolhido = randrange(1,5)
num = int(input("Adivinhe o numero que o computador pensou: "))
print("O computador pensou em:",escolhido)
if num == escolhido:
    print("PARABENS VOCÊ ACERTOU!")
else:
    print("Que pena.. Você errou")