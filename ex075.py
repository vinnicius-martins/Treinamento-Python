num = (int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")))
print("Numero de vezes que apareceu o valor 9:", num.count(9))
if 3 in num:
    print("Posição do primeiro valor 3:",num.index(3)+1)
else:
    print("Não foi encontrado o valor 3.")
print("Os valores pares: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")