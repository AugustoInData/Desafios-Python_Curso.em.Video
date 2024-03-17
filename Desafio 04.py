## Esse programa irá ler algo digitado pelo usuário
## e mostrará todas as informações sobre o que o usuário digitou

termo = input('Digite algo:')

print('O tipo primitivo desse valor é:', type(termo))
print('Só possui espaços?', termo.isspace())
print('É um número?',termo.isnumeric())
print('É alfabético?',termo.isalpha())
print('É alfanumérico?',termo.isalnum())
print('Está em maiúsculas?',termo.isupper())
print('Está em minúsculas?',termo.islower())
print('Está capitalizada?',termo.istitle())
