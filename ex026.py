frase = str(input("Digite uma frase: ").strip()).upper()
print("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A apareceu na posição", frase.find('A')+1)
print("A ultima letra A apareceu na posição", frase.rfind('A')+1)