## O programa irá ler o valor do cateto adjacente
## do cateto oposto, e em seguida, irá calcular
## o valor da hipotenusa

import math

cat_adj = float(input('Digite o valor do cateto adjacente:\n'))
cat_opo = float(input('Digite o valor do cateto oposto:\n'))

hip = math.hypot(cat_adj,cat_opo)

print(f'''Cateto adjacente: {cat_adj}
Cateto oposto: {cat_opo}
hipotenusa: {(hip):.2f}''')

