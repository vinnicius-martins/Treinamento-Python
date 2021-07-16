numeros = []
while True:
    num = int(input("Digite um numero: [999 para parar] "))
    if num == 999:
        break
    if numeros.count(num) >= 1:
        print("Esse numero ja existe na lista.")
    else:
        numeros.append(num)
numeros.sort()
print("Valores unicos digitados:", end=' ') 
for n in numeros:
    print(n, end=' ')   

