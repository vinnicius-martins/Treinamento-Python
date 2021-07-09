maior = 0
menor = 9999999
for i in range(1, 6):
    peso = float(input("Digite o peso da pessoa {}: ".format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('''O menor peso é {:.1f}KG
O maior peso é {:.1f}KG'''.format(menor, maior))