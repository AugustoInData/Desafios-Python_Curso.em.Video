## Esse programa irá calcular o valor de aluguel de um veículo
## perguntando os km rodados e quantos dias precisará alugar
## cada km custa R$ 0,15 e cada dia custa R$ 60,00

km = float(input('Quantos km você deseja percorrer com o veículo?\n'))
dias = int(input('Quantos dias você deseja alugar o veículo?\n'))

print(f'O preço do aluguel para percorrer {km}km durante {dias} é R${(km*0.15 + dias * 60)}')