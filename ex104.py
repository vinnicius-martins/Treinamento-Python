def leiaInt(txt):
    while True:
        msg = input(txt)
        if msg.isnumeric():
            break
        print('ERRO! Digite um numero inteiro.')
    return msg
    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')