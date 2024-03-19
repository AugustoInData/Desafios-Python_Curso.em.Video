## O programa irá verificar uma solicitação de empréstimo para o usuário
## o programa vai perguntar o valor da casa, o salário e em quantos anos
## o usuário pretenderá pagar 

valor_casa = float(input('Qual o valor do imóvel?\n'))
salario = float(input('Qual o seu salário?\n'))
tempo_pagamento = float(input('Em quantos anos você pretende pagar?\n'))

prestacao = valor_casa / (tempo_pagamento * 12)

if prestacao <= salario * (30 / 100):
    print('\033[34;45mSEU EMPRÉSTIMO FOI APROVADO!\033[m')
elif prestacao >= salario * (30 / 100):
    print('\033[35;41mSEU EMPRÉSTIMO NÃO FOI APROVADO!\033[m')