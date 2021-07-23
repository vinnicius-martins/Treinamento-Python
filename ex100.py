from random import randint
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))

def somaPar(lista):
    soma = 0 
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)
    
numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)