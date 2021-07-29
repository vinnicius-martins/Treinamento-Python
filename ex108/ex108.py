import moeda
from moeda import monetizar
preco = float(input("Digite o preço: R$")) 
print(f"A metade de {monetizar(preco)} é {monetizar(moeda.metade(preco))}")
print(f"O dobro de {monetizar(preco)} é {monetizar(moeda.dobro(preco))}")
print(f"Aumentando 10% de {monetizar(preco)} temos {monetizar(moeda.aumentar(preco))}")
print(f"Diminuindo 10% de {monetizar(preco)} temos {monetizar(moeda.diminuir(preco))}")