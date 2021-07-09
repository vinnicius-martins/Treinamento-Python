num = soma = count = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    count += 1
    soma += num
    num = int(input("Digite um numero [999 para parar]: "))
print("Voce digitou {} numeros e a soma entre eles foi {}.".format(count , soma))