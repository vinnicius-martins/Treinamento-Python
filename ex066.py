cont = soma = 0
while True:
    num = int(input("Digite o numero: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Foram digitados {cont} numeros e a soma entre eles é {soma}")