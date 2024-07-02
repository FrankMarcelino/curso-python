# desafio 015

#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e quantiadde de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

print('O total a pagar e de: R${:.2f}'.format((dias * 60) + (km * 0.15)))


