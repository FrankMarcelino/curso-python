# desafio 044

# Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto
# - a vista no cartão: 5% de desconto
# - em ate 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

import math

preco = float(input('digite o valor do produto: ')) #valor do produto

print('o valor do produto com 10% de desconto e: {}'.format (preco-(preco*10/100)))

