from random import shuffle
n1 = str(input("Primerio aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem da apresentação será {}".format(lista))