def fatorial(num, show=True):
    contador = 1
    if show:
        for c in range(num, 0, -1):
            contador *= c
            print(contador, end=' ')
            if c == 1:
                print()
    else:
        for c in range(num, 0, -1):
            contador *= c
    print(f'O fatorial de {num} é {contador}')        

fatorial(7)