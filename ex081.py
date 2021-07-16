numeros = []
while True:
    num = int(input("Digite um numero: [999 para parar] "))
    if num == 999:
        break
    numeros.append(num)
print(f'Numeros digitados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'Valores da lista: {numeros}')
if numeros.count(5) == 0:
    print("O valor 5 não foi digitado.")
else: 
    print("o valor 5 foi digitado na lista.")