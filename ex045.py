from random import randint
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada?''')
opc = int(input())
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
joga_pc = randint(0, 2)
print("O computador escolheu:",opcoes[joga_pc])
print("Você escolheu:",opcoes[opc])
if joga_pc == 0:
    if opc == 0:
        print("EMPATE")
    elif opc == 1:
        print("VOCÊ VENCEU!")
    elif opc == 2:
        print("VOCÊ PERDEU..")
    else:
        print("JOGADA INVALIDA")    
elif joga_pc == 1:
    if opc == 0:
        print("VOCÊ PERDEU..")
    elif opc == 1:
        print("EMPATE")
    elif opc == 2:
        print("VOCÊ VENCEU!")
    else:
        print("JOGADA INVALIDA") 
elif joga_pc == 2:
    if opc == 0:
        print("VOCÊ VENCEU!")
    elif opc == 1:
        print("VOCÊ PERDEU..")
    elif opc == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA") 