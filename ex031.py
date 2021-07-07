km = int(input("Digite a distancia da viagem em KM: "))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print("O preço da viagem é: R${:.2f}.".format(preco)) 