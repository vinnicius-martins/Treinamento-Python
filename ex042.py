l1 = int(input("Insira o comprimento da reta 1: "))
l2 = int(input("Insira o comprimento da reta 2: "))
l3 = int(input("Insira o comprimento da reta 3: "))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print("É possivel formar um triangulo:")
    if l1 == l2 and l2 == l3:
        print("EQUILATERO")
    elif l1 == l2 and l2 != l3:
        print("ISOSCELES")
    else:
        print("ESCALENO")
else:
    print("Não é possivel formar um triangulo.")
 