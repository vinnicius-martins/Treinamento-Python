from math import sqrt
oposto = float(input("Cateto oposto: "))
adj = float(input("Cateto adjacente: "))
hip = sqrt(oposto**2 + adj**2)
print("Hipotenusa = {:.2f}".format(hip))
