# desafio 018

#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('digite o valor do angulo: '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print('o angulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))