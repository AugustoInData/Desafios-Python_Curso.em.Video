## O programa vai mostrar a categoria de um atleta
## da natação com base em sua idade

from datetime import date
ano_atual = date.today().year

ano_nascimento = int(input('Qual ano você nasceu?\n'))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos. CATEGORIA MIRIM')
elif 14 >= idade > 9:
    print(f'Você tem {idade} anos. CATEGORIA INFANTIL')
elif 19 >= idade > 14:
    print(f'Você tem {idade} anos. CATEGORIA JUNIOR')
elif 25 >= idade > 19:
    print(f'Você tem {idade} anos. CATEGORIA SÊNIOR')
elif idade > 25:
    print(f'Você tem {idade} anos. CATEGORIA MASTER')