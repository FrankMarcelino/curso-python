# desafio 059

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar 
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa devera realizar a operação solicitada em cada caso.

while True:
  n1 = int(input('digite o primeiro numero: '))
  n2 = int(input('digite o segundo numero: '))
  print('''
  [ 1 ] somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números
  [ 5 ] sair do programa
  ''')
  op = int(input('qual sua opcao? '))
  if op == 1:
    print('a soma dos valores e: {}'.format(n1 + n2))
  elif op == 2:
    print('a multiplicacao dos valores e: {}'.format(n1 * n2))
  elif op == 3:
    if n1 > n2:
      print('o maior valor e: {}'.format(n1))
    elif n2 > n1:
      print('o maior valor e: {}'.format(n2))
    else:
      print('os valores sao iguais')
  elif op == 4:
    n1 = int(input('digite o primeiro numero: '))
    n2 = int(input('digite o segundo numero: '))
  elif op == 5:
    print('fim do programa')
    break
  else:
    print('opcao invalida, tente novamente!')
    
    
    
