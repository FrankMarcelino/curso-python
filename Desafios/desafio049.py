# desafio 049

# leia um numero inteiro e depois mostre na tela a sua tabuada

numero = int(input('digite um numero: '))

print('a tabuada de {} e:'.format(numero))

for c in range(1, 11):
  print('{} x {} = {}'.format(numero, c, numero * c))   

