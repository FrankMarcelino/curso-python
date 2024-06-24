# desafio 052

# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

numero = int(input('digite um numero: '))

for c in range(2, numero):
  if numero % c == 0:
    print('o numero {} NAO EH PRIMO'.format(numero, c))
    break
else:
  print('o numero {} é PRIMO'.format(numero))

  