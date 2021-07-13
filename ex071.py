cinq = vinte = dez = um = 0 
valor = int(input("Digite o valor a ser sacado: "))
while True:
    if valor >= 50:
        valor -= 50
        cinq += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    else:
        break
print(f'''Você recebeu:
{cinq} notas de 50
{vinte} notas de 20
{dez} notas de 10
{um} notas de 1''')