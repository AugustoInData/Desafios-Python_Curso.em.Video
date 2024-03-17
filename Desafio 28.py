## O programa irá escolher um número entre 1 e 5
## o usuário deverá adivinhar o número escolhido
## se o usuário acertar vai aparecer a mensagem:
## PARABÉNS, VOCÊ ACERTOU!!!
## se errar aparecerá: ERROOOOOU!!!

import random

num = [1,2,3,4,5]
pc = random.choice(num)
usuario_num = int(input('Adivinhe qual número o computador pensou entre 1 e 5:\n'))

if usuario_num == pc:
    print('PARABÉNS, VOCÊ ACERTOU!!!')
else:
    print('ERROOOOOU!!!')