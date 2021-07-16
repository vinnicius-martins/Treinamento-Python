pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Digite o nome: ")))
    dados.append(str(input("Digite o peso: ")))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opc = str(input("Quer continuar? [S/N]"))
    if opc in 'Nn':
        break
    elif opc in 'Ss':
        print(f'{"Proximo Cadastro":^10}')
print("Pessoas Cadastradas:", len(pessoas))
print("Pessoas mais pesadas: ",end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print("Pessoas mais leves: ",end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
