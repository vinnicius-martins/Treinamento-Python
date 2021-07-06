dias = int(input("Quantos dias? "))
km = float(input("Quantos Km percorridos? "))
dia = float(60)
km_rod = float(0.15)
total = dias*dia + km_rod*km
print("Preço final: R${:.2f}.".format(total))