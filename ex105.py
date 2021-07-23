def notas(*notas, sit=True):
    info = {}
    c = soma = 0
    info['qntd_notas'] = len(notas)
    info['maior'] = max(notas)
    info['menor'] = min(notas)
    while c < len(notas):
        soma += notas[c]
        c += 1
    media = soma / len(notas)
    info['media'] = media
    if media < 6:
        situacao = 'Ruim'
    elif 6 <= media < 8:
        situacao = 'Boa'
    else:
        situacao = 'Otima'
    if sit:
        info['situacao'] = situacao
    return info

print(notas(5.5, 2.5, 1.5))