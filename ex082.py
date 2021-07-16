lista1 = []
listapar = []
listaimpar = []
while True:
    num = int(input("Digite um numero: [999 para parar] "))
    if num == 999:
        break
    lista1.append(num)
for n in lista1:
    if n%2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(lista1)
print(listapar)
print(listaimpar)
