import moeda
preco = float(input("Digite o preço: R$"))
print(f"A metade de {preco} é R${moeda.metade(preco):.2f}")
print(f"O dobro de {preco} é R${moeda.dobro(preco):.2f}")
print(f"Aumentando 10% de {preco} temos R${moeda.aumentar(preco):.2f}")
print(f"Diminuindo 10% de {preco} temos R${moeda.diminuir(preco):.2f}")