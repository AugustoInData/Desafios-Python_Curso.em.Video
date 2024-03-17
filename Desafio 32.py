## Esse programa irá mostrar se um ano é bissexto

ano = int(input('Qual ano você deseja verificar se é bissexto?\n'))

div_4 = ano % 4
div_100 = ano % 100
div_400 = ano % 400

if div_4 == 0 and div_100 != 0 or div_400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
                
else:
    print(f'O ano de {ano} não é bissexto')