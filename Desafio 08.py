## O programa irá converter o valor em metro
## para centímetro e milímetro

metro = float(input('Quantos metros você deseja converter?:\n'))

cent = metro * 100
mili = metro * 1000

mensagem = f'O valor de {metro}m em centímetros é {cent}cm e em milímetros é {mili}mm'
print(mensagem)