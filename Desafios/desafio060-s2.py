# desafio 060

# Faca um programa que leia um numero qualquer e mostre o seu fatorial.

numero = int(input('digite um numero: '))
fatorial = 1
print('calculando {}! = '.format(numero), end='')
while numero > 0:
  print('{}'.format(numero), end='')
  print(' x ' if numero > 1 else ' = ', end='')
  fatorial *= numero
  numero -= 1
print('{}'.format(fatorial))