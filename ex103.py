def ficha(nome='Sem nome', gol=0):
    print(f'O jogador {nome} fez {gol} gols.')

nome = str(input('Nome do jogador: '))
gols = str(input(f'Gols de {nome}: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)