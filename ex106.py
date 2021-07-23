print('Interactive Help Python')
while True:
    comando = str(input("Digite o comando: "))
    if comando.upper() == 'FIM':
        break
    help(comando)
