## O programa irá ler o nome completo do usuário
## e vai mostrar qual o primeiro e o último nome

nome = str(input('Qual seu nome completo:\n')).strip().split()

print(f'Seu primeiro nome é: {(nome[0])}')
nome_total = int(len(nome))
print(f'Seu último nome é: {(nome[(nome_total)-1])}')