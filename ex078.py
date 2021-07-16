valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f"O maior valor digitado foi o {maior} e ele esta na(s) posição(ões): ", end='')
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(i, end='...')
print(f"\nO menor valor digitado foi o {menor} e ele esta na(s) posição(ões): ", end='')
for i, v in enumerate(valores):
    if valores[i] == menor:
        print(i, end='...')