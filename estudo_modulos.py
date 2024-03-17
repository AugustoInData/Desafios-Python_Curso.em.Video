texto = 'Curso em Vídeo Python'

print(texto[:13])
print(texto[5:])
print(texto[9::3])
print(len(texto))
print(texto.count('o'))
print(texto.find('deo'))
print(texto.find('android'))
print('Curso' in texto)

# texto.replace('Python','Android')

print(texto.upper())
print(texto.lower())

# o capitaliza deixa apenas a primeira letra maiúscula
print(texto.capitalize())

# o comando strip remove os espaços em branco antes e depois da frase
print(texto.strip())
# o rstrip removerá apenas os espaços em branco do lado direito 
# parecido com isso nós temos o comando lstrip que remove apenas 
# os espaços em branco do lado esquerdo
print(texto.rstrip())
# O comando split serve pra separar os termos de uma frase
print(texto.split())
print('-'.join(texto))
print(texto)
