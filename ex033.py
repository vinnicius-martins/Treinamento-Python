n1 = int(input("Digite o primeiro numero: "))
maior = n1
menor = n1
n2 = int(input("Digite o segundo numero: "))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = int(input("Digite o terceiro numero: "))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print("Maior:", maior)
print("Menor:", menor)
