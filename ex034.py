sal = float(input("Digite o salario do funcionario: R$"))
if sal > 1250:
    aum = sal * 1.10
else:
    aum = sal * 1.15
print("Seu novo salario é R${:.2f}".format(aum))