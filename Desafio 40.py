## O programa irá receber duas notas de um aluno 
## e irá calcular sua média. Em seguida, mostrará
## se ele foi aprovado, reprovado, ou recuperação

nota1 = float(input('Qual sua primeira nota:\n'))
nota2 = float(input('Qual a sua segunda nota?\n'))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média é {media}. APROVADO!!!')
elif media >= 5 and media < 7:
    print(f'Sua média é {media}. RECUPERAÇÃO') 
elif media < 5:
    print(f'Sua média é {media}. REPROVADO')
else:
    print('VOCÊ DIGITOU ERRADO')