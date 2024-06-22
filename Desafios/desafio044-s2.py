# desafio 044

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/PIX: 10% de desconto
# - Debito ou no cartão: preco normal
# - em 2x ou mais no cartão: acrescentar juros de 5% por mês


import math

preco = float(input('digite o valor do produto: ')) #valor do produto

formaDePagamento = int(input('''digite a forma de pagamento:
[ 1 ] a vista dinheiro/PIX
[ 2 ] Debito ou no cartão para o vencimento
[ 3 ] 2x ou mais no cartão
''')) #forma de pagamento



if formaDePagamento == 1: #forma de pagamento a vista dinheiro/pix
  print('o valor final do seu produto e: R${:.2f}'.format(preco - (preco * 0.10)))
elif formaDePagamento == 2: #forma de pagamento debito ou no cartão para o vencimento
  print('o valor final do seu produto e: R${:.2f}'.format(preco))
elif formaDePagamento == 3: #forma de pagamento em 2x ou mais no cartão
  parcelas = int(input('quantas parcelas? '))
  precoPorParcela = math.ceil(preco / parcelas + (preco * 0.05))
  if parcelas >= 2:
    print('você parará em {}x de R${:.2f} com juros'.format(parcelas, precoPorParcela))
    print('o valor final do seu produto e: R${:.2f}'.format(precoPorParcela * parcelas))
else:
  print('forma de pagamento invalida')
  





