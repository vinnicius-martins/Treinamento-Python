jogadores = []
jogador = {}
partidas = []
while True:
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    jogador['partidas'] = int(input("Quantas partidas ele jogou? "))
    for i in range(0, jogador['partidas']):
        gols = int(input(f"Quantos gols na partida {i+1}? "))
        partidas.append(gols)
    jogador['gol'] = partidas[:]
    jogador['tot_gol'] = sum(partidas) 
    jogadores.append(jogador.copy())
    opc = str(input("Quer continuar? [S/N] "))
    if opc in 'Nn':
        break
for j in jogadores:
    print(j)