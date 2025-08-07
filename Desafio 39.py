## Esse programa vai perguntar o ano de nascimento do usuário
## em seguida mostrará se ele está novo para se alistar no exército,
## se está na hora do alistamento, e se já passou da hora. Além disso
## também mostrará quanto tempo falta para se alistar ou quanto tempo passou

from datetime import date
atual = date.today().year

print('-=-' * 20)
print('VAMOS VERIFICAR SE VOCÊ ESTÁ APTO PARA O ALISTAMENTO MILITAR')
print('-=-' * 20)

ano = int(input('QUAL ANO VOCÊ NASCEU?\n'))

idade = atual - ano
passou = idade - 18
falta = 18 - idade

if idade == 18:
    print('VOCÊ PODE SE ALISTAR NESSE ANO')
elif idade < 18:
    print('VOCÊ NÃO PODE SE ALISTAR')
    print(f'FALTA {falta} ANOS PARA VOCÊ PODER SE ALISTAR')
elif idade > 18:
    print('VOCÊ JÁ DEVERIA TER SE ALISTADO')
    print(f'JÁ PASSOU {passou} ANOS DO TEMPO DE VOCÊ SE ALISTAR')