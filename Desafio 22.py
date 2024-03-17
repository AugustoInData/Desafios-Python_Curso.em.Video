## O programa irá ler o nome completo do usuário
## Após isso irá mostrar:
## - O nome só com letras maiúsculas
## - O nome só com letras minúsculas
## - Contará quantas letras possui (sem considerar espaços)
## - Contará quantas letras tem no primeiro nome

nome = input('Digite seu nome completo:\n')

print(f'Seu nome em letras maiúsculas é: {(nome.upper())}')

print(f'Seu nome em letras minúsculas é: {(nome.lower())}')

print(f'Seu nome tem {(len(nome.replace(" ","")))} letras')

nome_lista = nome.split()
print(f'Seu primeiro nome tem {(len(nome_lista[0]))} letras')