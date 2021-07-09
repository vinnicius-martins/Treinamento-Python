sexo = str(input("Insira seu sexo: ")).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input("Dados Invalidos. Por favor, Insira seu sexo: ")).strip().upper()[0]
    