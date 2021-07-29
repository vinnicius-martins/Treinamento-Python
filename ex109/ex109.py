import moeda
from moeda import monetizar
preco = float(input("Digite o preço: R$"))
opc = str(input("Deseja monetizar? [S/N]"))
opc2 = True
if opc in 'Nn':
    opc2 = False
print(f"A metade de {monetizar(preco, opc2)} é {moeda.metade(preco, opc2)}")
print(f"O dobro de {monetizar(preco, opc2)} é {moeda.dobro(preco, opc2)}")
print(f"Aumentando 10% de {monetizar(preco, opc2)} temos {moeda.aumentar(preco, opc2)}")
print(f"Diminuindo 10% de {monetizar(preco, opc2)} temos {moeda.diminuir(preco, opc2)}")