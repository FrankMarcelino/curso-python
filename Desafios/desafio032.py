# desafio 032

# Faca um programa que leia um ano qualquer e mostre se ele e bissexto

ano = int(input('digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('o ano {} e bissexto'.format(ano))
else:
  print('o ano {} nao e bissexto'.format(ano))

