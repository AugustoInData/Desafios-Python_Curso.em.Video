## Esse programa irá mostrar se um número é par ou ímpar

num = int(input('Digite um número:\n'))

resto = num % 2

if resto == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')