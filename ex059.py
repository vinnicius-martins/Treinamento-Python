n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
opc = 0
while opc != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opc = int(input("Opção: "))
    if opc == 1:
        total = n1+n2
    elif opc == 2:
        total = n1*n2
    elif opc == 3:
        if n1 > n2:
            total = n1
        if n2 > n1:
            total = n2
        else: 
            total = 'Os valores são iguais'
    elif opc == 4:
        print("Digite os numeros novamente.")
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
    else:
        print("Opção invalida! Tente novamente.")
    if str(opc) in '123':
        print("Total:", total)