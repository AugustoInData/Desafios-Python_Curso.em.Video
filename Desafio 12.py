## O programa irá calcular 5% de desconto no preço de um produto

print('-=-' * 20)
print('\033[34;33mESTAMOS COM PROMOÇÃO DE 5% DE DESCONTO EM QUALQUER PRODUTO DE NOSSA LOJA!\033[m')
print('-=-' * 20)
preco = float(input('Qual o valor do produto?\n'))

desconto = preco - preco * (5 / 100)

print(f'Esse produto de R${preco} vai ficar por R${(desconto):.2f} com 5% de desconto')