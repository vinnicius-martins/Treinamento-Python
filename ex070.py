soma = mais_1000 = barato = cont = 0
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Insira o preço do produto: R$"))
    soma += preco
    cont += 1
    if cont == 1:
        barato = preco
        mais_barato = nome
    else:
        if preco < barato:
            barato = preco
            mais_barato = nome
    if preco > 1000:
        mais_1000 += 1
    opc = str(input("Quer continuar? [S/N] "))
    if opc in 'Nn':
        break
print(f'''Quantidade de produtos: {cont}
Total da compra: R${soma:.2f}
Quantidade de produtos que custam mais de R$1000: {mais_1000}
Nome do produto mais barato: {mais_barato}''')
