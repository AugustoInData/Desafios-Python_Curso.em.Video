## Esse programa irá ler um número e mostrará seu sucessor e seu antecessor

num = int(input('Digite um número:'))

ante = num - 1
suce = num + 1

mensagem = f'O número que você digitou foi o {num}, seu antecessor é {ante} e o sucessor é o {suce}!'

print(mensagem)
