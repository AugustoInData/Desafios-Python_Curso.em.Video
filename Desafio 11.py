## O programa vai ler a altura e a largura de uma parede
## em seguida irá calcular a área e quantos litros de tinta
## são necessários para pintá-la
## obs: 1L de tinta pinta 2m²

altura = float(input('Qual a altura da parede:\n'))
largura = float(input('Qual a largura da parede:\n'))

area = altura * largura
## a variável litros verifica quantos litros são necessários para pintar a 
## área total da parede
litros = area / 2

print(f'A altura da parede é: {altura}m\nA largura é: {largura}m\nA área da parede é: {area}m²\nPara pintar essa parede serão necessários {litros}L de tinta\n')