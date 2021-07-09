from datetime import date
menores = 0
maiores = 0 
ano = [0]*7
for i in range(1, len(ano)+1):
    ano[i-1] = int(input("INSIRA O ANO DE NASCIMENTO DA PESSOA [{}]: ".format(i)))
    print(ano[i-1])
    idade = date.today().year - ano[i-1]
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('''Quantidade de pessoas menores de idade: {}
Quantidade de pessoas maiores de idade: {}'''.format(menores, maiores))