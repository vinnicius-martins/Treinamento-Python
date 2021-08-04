def leiaInt(txt):
    while True:
        try:
            msg = int(input(txt))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um numero inteiro valido.')
            continue
        else:
            return int(msg)

def linha(tam=42):
    return print('-' * tam)

def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaInt('Sua Opção: ')
    return opc
    

num = [2, 8, 4, 7]
num.ins