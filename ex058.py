from random import randrange
escolhido = randrange(1,10)
num = 11
while num != escolhido:
    num = int(input("Adivinhe o numero que o computador pensou: "))
    if num < escolhido:
        print("Mais.. Tente Novamente")
    if num > escolhido:
        print("Menos... Tente Novamente")
print("Parabens você acertou!!")
