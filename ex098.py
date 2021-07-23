def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i, end=' ')
    print()
    print('-+'*30)

print('Contagem de 1 até 10, de 1 em 1')
contador(1, 10, 1)

print('Contagem de 10 até 0, de 2 em 2')
contador(10, -2, -2)

print('Agora é sua vez de escolher a contagem!')
ini = int(input("Inicio: "))
fi = int(input("Fim: "))
pas = int(input("Passo: "))

if ini < fi:
    contador(ini, fi, pas)
elif fi < ini:
    passo_neg = pas - pas*2
    contador(fi, ini, pas)
else:
    print(ini)

