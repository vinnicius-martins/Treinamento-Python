def monetizar(valor, monetiza=True):
    if monetiza:
        valor = (f'R${valor:.2f}')
    return valor

def aumentar(preco, monetiza=True):
    preco *= 1.10
    if monetiza:
        monetizar(preco)
    return preco

def diminuir(preco, monetiza=True):
    preco *= 0.90
    if monetiza:
        monetizar(preco)
    return preco

def dobro(preco, monetiza=True):
    preco *= 2
    if monetiza:
        monetizar(preco)
    return preco

def metade(preco, monetiza=True):
    preco /= 2
    if monetiza:
        monetizar(preco)
    return preco