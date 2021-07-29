def monetizar(valor):
    valor = (f'R${valor:.2f}')
    return valor

def aumentar(preco):
    preco *= 1.10
    return preco

def diminuir(preco):
    preco *= 0.90
    return preco

def dobro(preco):
    preco *= 2
    return preco

def metade(preco):
    preco /= 2
    return preco