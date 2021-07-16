from random import randint
maior = menor = 0
valores = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print("Eu sorteei os valores:", end=" ")
for i in valores:
    print(i, end=" ")
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
