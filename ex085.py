valores = [[],[]]
for i in range(0, 7):
    num = int(input(f"Digite o {i+1}o valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(valores)
    