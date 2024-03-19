## O programa irá ler o salário de um funcionário
## e irá calcular seu aumento com reajuste de 15%

print('\033[34m-=-\033[m' * 20)
print('\033[4;34;43mVamos calcular seu reajuste salarial\033[m')
print('\033[34m-=-\033[m' * 20)

salario = float(input('Qual o seu salário?\n'))

reajuste = salario * (15 / 100) + salario

print(f'Seu salário reajustado será de R${(reajuste):.2f}')