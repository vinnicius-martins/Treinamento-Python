from datetime import date
ano_nasc = int(input("Qual o ano de nascimento do atleta? "))
idade = date.today().year - ano_nasc
print("CATEGORIA: ")
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SENIOR")
elif idade > 25:
    print("MASTER")