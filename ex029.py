velo = int(input("Digite a velocidade do carro: "))
if velo > 80:
    multa = (velo-80)*7
    print("Você foi multado em R${:.2f}".format(multa))
else:
    print("Ufa.. Sem multa pra você")