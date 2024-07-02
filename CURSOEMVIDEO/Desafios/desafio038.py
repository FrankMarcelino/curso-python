# desafio 038

# Escreva um programa que leia dois numeros inteiros e compare-os. mostrando na tela uma mensagem:

# - O primeiro valor e maior
# - O segundo valor e maior
# - Não existe valor maior, os dois sao iguais

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

if n1 > n2:
  print('o primeiro valor e maior')
elif n2 > n1:
  print('o segundo valor e maior')
else:
  print('os dois valores sao iguais')

