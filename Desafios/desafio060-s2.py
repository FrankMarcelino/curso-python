# desafio 060
#mudei o desafio para ficar mais complexo
# Faca um programa que leia um numero qualquer e mostre o seu fatorial.
# Faça um menu que mostre a 2 opções: 1 ultilizando while e 2 utilizando for.

while True:
  print('''
  [ 1 ] while
  [ 2 ] for
  ''')
  op = int(input('qual sua opcao? '))
  if op == 1:
    numero = int(input('digite um numero: '))
    fatorial = 1
    print('calculando {}! = '.format(numero), end='')
    while numero > 0:
      print('{}'.format(numero), end='')
      print(' x ' if numero > 1 else ' = ', end='')
      fatorial *= numero
      numero -= 1
      print('{}'.format(fatorial))
    break
  elif op == 2:
    numero = int(input('digite um numero: '))
    fatorial = 1
    print('calculando {}! = '.format(numero), end='')
    for c in range(numero, 0, -1):
      print('{}'.format(c), end='')
      print(' x ' if c > 1 else ' = ', end='')
      fatorial *= c
      print('{}'.format(fatorial))
    break
  else:
    print('opcao invalida, tente novamente!')
    
    

