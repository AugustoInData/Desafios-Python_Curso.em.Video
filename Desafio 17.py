## O programa irá ler um número e seguida mostrará sua parte inteira

import math
num = float(input('Digite um número:\n'))

parte_inteira = math.trunc(num)

print(f' O número digitado foi {num} e sua parte inteira é {parte_inteira}')