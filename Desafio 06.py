## Esse programa irá ler um número e mostrará:
## o dobro, o triplo e a raiz quadrada

num = int(input('Digite um número:\n'))

dobro = num * 2
triplo = num * 3
raiz_quad = num ** (1 / 2)

mensagem = f'Você digitou o número {num}!\nSeu dobro é: {dobro}\nSeu triplo é: {triplo}\nSua raiz quadrada é: {raiz_quad}'
print(mensagem)