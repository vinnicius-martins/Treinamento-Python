pessoas = []
dados = []
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    pessoas.append(dados[:])
    dados.clear()
    opc = str(input("Quer continuar? [S/N] "))
    if opc in 'Nn':
        break
print("-="*11)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print("-="*11)
for c, p in enumerate(pessoas):
    media = (p[1]+p[2])/2
    print(f'{c:<4}{p[0]:<10}{media:>8}')
print("-="*11)
while True:
    aluno = int(input("Mostrar notas de qual aluno? [999 interrompe] "))
    if aluno == 999:
        break
    print(f'Notas de {pessoas[aluno][0]}: {pessoas[aluno][1]}, {pessoas[aluno][2]}')
    