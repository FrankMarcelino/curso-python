# desafio 064
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

print('digite 999 para parar o programa')

soma = 0
cont = 0

while True:
  num = int(input('digite um numero: '))

  if num == 999:
    break

  soma += num
  cont += 1

print('a soma dos {} numeros digitados e: {}'.format(cont, soma))

