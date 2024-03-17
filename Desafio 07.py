## O programa irá ler duas notas de um aluno
## e mostrará a sua média

nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota'))

media = (nota1 + nota2) / 2

mensagem = f'A primeira nota foi {nota1}, a segunda foi {nota2}, então, a média é: {media}'
print(mensagem)