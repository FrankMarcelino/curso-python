# desafio 17
# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.

import math

catetoOp = float(input('digite o valor do cateto oposto: '))
catetoAdj = float(input('digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(catetoOp, catetoAdj)

print('o valor da hipotenusa e: {}'.format(hipotenusa))