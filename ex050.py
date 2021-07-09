soma = 0
for i in range(1,7):
    n = int(input("Digite o numero [{}]: ".format(i)))
    if n % 2 == 0:
        soma += n
print("A soma dos numeros pares é {}".format(soma))