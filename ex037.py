num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversâo:
[ 1 ] Converter para binario
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal''')
opc = int(input("Sua opçao: "))
if opc == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print("Opção invalida! Tente novamente.")