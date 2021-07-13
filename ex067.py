while True:
    valor = int(input("Insira um numero: "))
    if valor < 0:
        break
    print("{:=^20}".format("TABUADA"))
    for i in range(1,11):
        print("{:^20}".format("{} x {} = {}".format(valor, i, valor*i)))