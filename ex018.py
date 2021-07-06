from math import radians, sin, cos, tan
angulo = float(input("Digite o angulo: "))
rad = radians(angulo)
sen = sin(rad)
cosse = cos(rad)
tang = tan(rad)
print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(sen, cosse, tang))