from datetime import datetime
trabalhador = {}
trabalhador['nome'] = str(input("Digite o nome: "))
nasc = int(input("Digite o ano de nascimento: "))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['carttrab'] = int(input("Digite a carteira de trabalho: [0 não tem] "))
if trabalhador['carttrab'] != 0:
    trabalhador['ano-contr'] = int(input("Digite o ano de contratação: "))
    trabalhador['sal'] = float(input("Digite o salario: R$"))
    trabalhador['aposenta'] = trabalhador['idade'] + (trabalhador['ano-contr'] + 35)  - datetime.now().year
print(trabalhador)