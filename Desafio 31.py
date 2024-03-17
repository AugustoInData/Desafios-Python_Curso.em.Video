## Esse programa irá calcular o preço de uma passagem
## para viagens de até 200 km será cobrado R$ 0,50 por km
## para viagens acima disso será cobrado R$ 0,45 por km

distancia = float(input('Qual a distância será percorrida na viagem?\n'))

if distancia <= 200:
    val_passagem = distancia * 0.50
    print(f'O preço da passagem para uma distância de {distancia}km é R${(val_passagem):.2f}')
else:
    val_passagem = distancia * 0.45
    print(f'O preço da passagem para a distância de {distancia}km é R${(val_passagem):.2f}')