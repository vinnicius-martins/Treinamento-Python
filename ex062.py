termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10-1)* razao
total = 0
mais_quantos = 10
while mais_quantos != 0:
    while termo <= mais_quantos:
        print(termo, end=" -> ")
        termo += razao
        print("PAUSA" if termo == decimo else "")

