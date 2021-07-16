from random import randint
jogo = []
numeros = []
qtd = int(input("Quantos jogos serão gerados? "))
cont = 0
for i in range(0, qtd):
    while True:
        num = randint(1,60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    jogo.append(numeros[:])
    numeros.clear()
for c, n in enumerate(jogo):
    print(f'Jogo {c+1}: {n}')
