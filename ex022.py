nome = input("Digite seu nome completo: ").strip()
print("Nome em maiusculas:",nome.upper())
print("Nome em minusculas:",nome.lower())
dividido = nome.split()
print("Letras ao todo:",len(nome)-nome.count(" "))
print("Letras do primeiro nome:",len(dividido[0]))