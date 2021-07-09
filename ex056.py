soma_idade = float(0)
maior = 0
mulheres_20 = 0
for i in range(1, 5):
    nome = str(input("[{}] Digite o nome: ".format(i)))
    idade = int(input("[{}] Digite a idade: ".format(i)))
    sexo = str(input("[{}] Digite o sexo [M/F]: ".format(i)))
    print("=-"*15)
    soma_idade += idade
    if sexo in ('Mm') and idade > maior:
        maior = idade
        mais_velho = nome
    if sexo in ('Fm') and idade < 20:
        mulheres_20 += 1 
media_idade = soma_idade/4     
print('''A media das idades do grupo: {}
O homem mais velho: {}
Mulheres com menos de 20 anos: {}'''.format(media_idade, mais_velho, mulheres_20))