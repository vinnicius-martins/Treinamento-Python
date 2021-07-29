def leiaInt(txt):
    while True:
        try:
            msg = int(input(txt))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um numero inteiro valido.')
            continue
        else:
            return int(msg)

def leiaFloat(txt):
    while True:
        try:
            msg = float(input(txt))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um numero real valido.')
            continue
        else:
            return int(msg)
    
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o numero inteiro {n}.')

n = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o numero real {n}.')