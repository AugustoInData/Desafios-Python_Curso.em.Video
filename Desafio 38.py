## Esse programa irá ler dois números e compará-los
## dizendo qual o maior e qual o menor

num1 = int(input('Digite o primeiro número:\n'))
num2 = int(input('Digite o segundo número:\n'))

print(f'O primeiro número escolhido foi o {num1}')
print(f'O segundo número escolhido foi o {num2}')

if num1 > num2:
    print(f'O primeiro valor é maior, pois {num1} é maior que {num2}')
elif num1 == num2:
    print('OS DOIS NÚMEROS SÃO IGUAIS!')
else:
    print(f'O segundo número é maior, pois {num2} é maior que {num1}')