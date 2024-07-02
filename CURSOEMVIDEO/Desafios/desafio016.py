# desafio 016
# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input('digite um numero real: '))

print('a porção inteira de {} e: {}'.format(num, math.trunc(num)))
