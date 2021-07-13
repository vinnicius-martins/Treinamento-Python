mais_18 = homens = mulheres_menos_20 = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: [M/F]"))
    if idade > 18:
        mais_18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20 += 1
    opc = str(input("Quer continuar? [S/N]"))
    if opc in 'Nn':
        break
print(f'''Pessoas com mais de 18 anos: {mais_18}
Homens: {homens}
Mulheres com menos de 20 anos: {mulheres_menos_20}''')