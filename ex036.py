casa = float(input("Digite o valor da casa: R$"))
sal = float(input("Insira o salario: R$"))
anos = int(input("Em quantos anos vai pagar? "))
prest = casa/(12*anos)
prest_max = sal * 0.3
if prest <= prest_max:
    print("Prestação mensal: R${:.2f}.".format(prest))
    print("Duração: {} meses.".format(anos*12))
else:
    print("Prestação máxima: R${:.2f}".format(prest_max))
    print("Prestação necessaria: R${:.2f}.".format(prest))
    print("Emprestimo negado.")
