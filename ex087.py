matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma3 = maior2 = somapar = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior2:
                maior2 = matriz[i][j]
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()
print(f'A soma de todos os valores pares: {somapar}')
print(f'A soma dos valores da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha: {maior2}')