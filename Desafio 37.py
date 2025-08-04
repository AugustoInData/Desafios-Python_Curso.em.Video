## O programa irá perguntar para o usuário
## qual conversão ele pretende fazer, se é para
## binário, octal ou hexadecimal


print('Posso fazer a conversão de um número para binário, octal ou hexadecimal')
num = int(input('Qual valor você pretende converter?\n'))
pergunta = str(input('Qual sua opção você prefere?\n')).upper().strip()

bina = 'BINÁRIO'
octa = 'OCTAL'
hexa = 'HEXADECIMAL'

if pergunta == bina:
    print(f'O valor {num} convertido para binário é {bin(num)}')
elif pergunta == octa:
    print(f'O valor {num} convertido para octal é {oct(num)}')
elif pergunta == hexa:
    print(f'O valor {num} convertido para hexadecimal é {hex(num)}')
else:
    print('ESCREVA CORRETAMENTE!')