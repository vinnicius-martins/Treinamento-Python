opc = 'S'
maior = cont = soma = menor = 0

while opc in 'Ss':
    num = int(input("Digite um numero: "))
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    opc = str(input("Quer continuar? [S/N]"))
print("Você digitou {} numeros e a media foi {:.2f}".format(cont, soma/cont))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))