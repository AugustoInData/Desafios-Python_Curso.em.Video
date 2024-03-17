## Esse programa vai verificar se um motorista
## levará uma multa, caso tenha ultrapassado
## 80km/h. O programa também calculará o valor
## da multa, sendo que, cada km ultrapassado
## custa R$  7,00

velocidade = float(input('Qual a velocidade o carro estava?:\n'))

if velocidade > 80:
    print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE E SERÁ MULTADO!!!')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa é R${(multa):.2f}')

else:
    print('VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE')