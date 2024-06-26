# desafio 066
# Crie um programa que leia varios números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = 0
cont = 0
num = 0

while True:
  print('digite 999 para parar')
  num = int(input('digite um numero: '))
  if num == 999:
    break
  soma += num
  cont += 1
print('a soma dos {} numeros digitados e: {}'.format(cont, soma))

