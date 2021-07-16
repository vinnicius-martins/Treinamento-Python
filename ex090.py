aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a media do aluno: "))
if aluno['media'] >= 7:
    situacao = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
aluno['situacao'] = situacao
for k, v in aluno.items():
    print(f'{k} = {v}')