peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print("O imc é: {:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Peso ideal")
else:
    print("Obesidade morbida")

