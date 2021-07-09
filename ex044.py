preco = float(input("Digite o preço do produto: R$"))
print('''Como deseja pagar?
1 - À VISTA DINHEIRO/CHEQUE
2 - À VISTA NO CARTÃO
3 - EM ATÉ 2X NO CARTÃO
4 - 3X OU MAIS NO CARTÃO''')
opc = int(input())
if opc == 1:
    print("O valor a ser pago é de R${:.2f}".format(preco*0.9))
elif opc == 1:
    print("O valor a ser pago é de R${:.2f}".format(preco*0.95))
elif opc == 1:
    print("O valor a ser pago é de R${:.2f}".format(preco))
elif opc == 1:
    print("O valor a ser pago é de R${:.2f}".format(preco*1.20))
else:
    print("Opção invalida! Tente novamente.")