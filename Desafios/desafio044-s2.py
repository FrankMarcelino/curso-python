# desafio 044

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto
# - a vista no cartão: 5% de desconto
# - em ate 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

import math

preco = float(input('digite o valor do produto: ')) #valor do produto

formaDePagamento = int(input('''digite a forma de pagamento:
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')) #forma de pagamento

if formaDePagamento == 1: #forma de pagamento a vista dinheiro/cheque
  print('o valor final do seu produto e: R${:.2f}'.format(preco - (preco * 0.10)))
elif formaDePagamento == 2: #forma de pagamento a vista no cartão
  print('o valor final do seu produto e: R${:.2f}'.format(preco - (preco * 0.05)))
elif formaDePagamento == 3: #forma de pagamento em 2x no cartão
  print('o valor final do seu produto e: R${:.2f}'.format(preco))
elif formaDePagamento == 4: #forma de pagamento em 3x ou mais no cartão
  print('o valor final do seu produto e: R${:.2f}'.format(preco + (preco * 0.20)))
else:
  print('forma de pagamento invalida')
  





