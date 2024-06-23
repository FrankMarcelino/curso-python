# desafio 051

# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))

for c in range(primeiroTermo, (primeiroTermo + (10 * razao)), razao):
  print(c, end=' ')