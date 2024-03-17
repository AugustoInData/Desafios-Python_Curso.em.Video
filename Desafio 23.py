## O programa irá ler um número
## de 0 a 9999, e em seguida, vai
## exibir separadamente a unidade, a dezena
## a centena e o milhar

num = (input('Digite um número entre 0 e 9999\n'))

espaco = num.replace(""," ")
num_lista = espaco.split()

print(num_lista)

print(f'Unidade: {num_lista[3]}')
print(f'Dezena: {num_lista[2]}')
print(f'Centena: {num_lista[1]}')
print(f'Milhar: {num_lista[0]}')