from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    print(f'Com {idade} anos: ',end='')
    if idade < 16:
        print('VOTO NEGADO.')        
    elif 16 <= idade < 18:
        print('VOTO OPCIONAL.') 
    else:
        print('VOTO OBRIGATÓRIO.')
    
print('-'*30)
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))