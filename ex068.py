from random import randint
cont = 0
while True:
    n1 = randint(1,10)
    n2 = int(input("Digite o numero: "))
    opc = str(input("Par ou Impar? [P/I} "))
    if opc in 'Pp' and (n1+n2) % 2 == 0:
        print("Você venceu!!")
        print("Jogue novamente")
        cont += 1
    else:
        print("Você Perdeu..")
        print(f"Vitorias consecutivas: {cont}")
        break