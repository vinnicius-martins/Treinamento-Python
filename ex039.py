nasc = int(input("Digite o ano do seu nascimento: "))
ano = int(input("Em qual ano estamos? "))
idade = ano - nasc
if idade == 18:
    print("É hora exata de se alistar.")
elif idade > 18:
    print("Você passou do praso de alistamento tem {} ano(s).".format(idade-18))
else:
    print("Você irá se alistar daqui a {} ano(s)".format(18-idade))