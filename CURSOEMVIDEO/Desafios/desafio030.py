# desafio 030
# Crie um programa que leia um numero inteiro e mostre na tela se ele e par ou impar

numero = int(input('digite um numero: '))

if numero % 2 == 0:
  print('o numero {} e par'.format(numero))
else:
  print('o numero {} e impar'.format(numero))

