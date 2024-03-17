## O programa irá analisar o nome de um cidade
## digitada pelo usuário, e em seguida, 
## responderá se a cidade começa com a palavra "Santo"

cidade = str(input('Digite o nome de uma cidade:\n')).strip()

print(cidade[:6].upper() == 'SANTO')