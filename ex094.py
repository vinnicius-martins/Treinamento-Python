pessoas = []
dados = {}
soma = 0 
while True:
    dados['nome'] = str(input("Digite o nome: "))
    while True:
        dados['sexo'] = str(input("Sexo: [M/F] "))
        if dados['sexo'] in 'MFmf':
            break
        print("Valor invalido! Digite somente M ou F.")
    dados['idade'] = int(input("Idade: "))
    pessoas.append(dados.copy())
    soma += dados['idade']
    opc = str(input("Quer continuar? [S/N] "))
    if opc in 'Nn':
        break
print(pessoas)
print('Pessoas cadastradas:', len(pessoas))
print("Média das idades: ", soma/ len(pessoas))
print("Mulheres cadastradas: ")
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print("\nPessoas com idade acima da médias: ")
for p in pessoas:
    if p['idade'] > soma/len(pessoas):
        print(p['nome'], end=' ')