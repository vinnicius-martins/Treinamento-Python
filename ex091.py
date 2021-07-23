from random import randint
print("Valores sorteados:")
jogadores = []
jogador = {}
ranking = {}
for i in range(0,4):
    jogador['nome'] = (f'jogador{i+1}')
    jogador['dado'] = randint(1,6)
    jogadores.append(jogador.copy())
ranking = sorted(jogadores, key=lambda row:row['dado'], reverse=1)
for lugar in ranking:
    print(lugar)