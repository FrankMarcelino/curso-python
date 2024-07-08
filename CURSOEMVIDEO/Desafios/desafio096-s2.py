# desafio 96

# faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
  return l * c

l = float(input('digite a largura: '))
c = float(input('digite o comprimento: '))

print('a area do terreno e: {}m2'.format(area(l, c)))