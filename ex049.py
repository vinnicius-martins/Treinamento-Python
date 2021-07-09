valor = int(input("Insira um numero: "))
print("{:=^20}".format("TABUADA"))
for i in range(1,11):
    print("{:^20}".format("{} x {} = {}".format(valor, i, valor*i)))