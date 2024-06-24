# desafio 052

# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

numero = int(input('digite um numero: '))
totalDeNumerosDivididos = 0
for c in range(1, numero + 1):
  if numero % c == 0:
    print('\33[33m', end='')
    totalDeNumerosDivididos += 1
   
  else:
    print('\33[31m', end='')
  print('{}'.format(c), end='')
print( '\n\033[m O numero {} foi divisivel {} vezes'.format(numero, totalDeNumerosDivididos))
if totalDeNumerosDivididos == 2:
  print('e por isso ele e um numero primo')
else:
  print('e por isso ele nao e um numero primo')

 

  