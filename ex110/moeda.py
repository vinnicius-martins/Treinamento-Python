def monetizar(valor):
    valor = (f'R${valor:.2f}')
    return valor

def aumentar(preco, aum):
    preco += (preco*aum)/100
    monetizar(preco)
    return preco

def diminuir(preco, dim):
    preco -= (preco*dim)/100
    monetizar(preco)
    return preco

def dobro(preco):
    preco *= 2
    monetizar(preco)
    return preco

def metade(preco):
    preco /= 2
    monetizar(preco)
    return preco

def resumo(preco=0, aum=10, dim=5):
    print('='*30)
    print("RESUMO DO VALOR".center(30))
    print('='*30)
    print(f'Preço analisado: {monetizar(preco)}')
    print(f'Dobro do preço: {dobro(preco)}')
    print(f'Metade do preço: {metade(preco)}')
    print(f'{aum}% de aumento: {aumentar(preco, aum)}')
    print(f'{dim}% de redução: {diminuir(preco, dim)}')
    