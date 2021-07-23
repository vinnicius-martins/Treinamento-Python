def area(larg, comp):
    area = larg*comp
    print(f'Area do terreno: {area:.1f}m2')

lar = float(input("Insira a largura do terreno: (m)"))
compr = float(input("Insira o comprimento do terreno: (m)"))
area(lar, compr)