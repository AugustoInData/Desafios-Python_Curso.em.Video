## O programa irá ler uma frase escrita pelo usuário
## em seguida mostrará:
## - quantas vezes a letra "a" aparece
## - qual posição ela aparece primeiro
## - qual posição ela aparece por último

frase = str(input('Digite uma frase:\n')).lower().strip()

print(f'A letra A aparece {(frase.count('a'))} vezes na frase')
print(f'A letra A aparece a primeira vez na posição {(frase.find('a')+1)}')
print(f'A última letra A aparece na posição {(frase.rfind('a')+1)}')
