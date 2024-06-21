# desafio 036

# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo ser negado.

casa = float(input('digite o valor da casa: '))
salario = float(input('digite o valor do seu salario: '))
anos = int(input('digite em quantos anos deseja pagar: '))

prestacao = casa / (anos * 12)

if prestacao > (salario * 0.30):
  print('a prestação ficou em {:.2f}'.format(prestacao))
  print('Emprestimo negado')
  print('O valor da prestacao ultrapassa 30% do seu salario')
else:
  print('Emprestimo aprovado')
  print('O valor da prestacao ficou em {:.2f}'.format(prestacao))

