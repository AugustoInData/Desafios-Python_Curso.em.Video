## O programa irá ler o nome do usuário
## e em seguida vai dizer se tem "Silva"
## em seu nome

nome = str(input('Qual seu nome completo:\n')).strip()

confirmando = nome.upper().find('SILVA') > 0
print(confirmando)




