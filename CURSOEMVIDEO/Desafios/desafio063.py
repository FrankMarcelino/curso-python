# desafio 063
# Crie um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('digite um numero: ')) 

t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
  t3 = t1 + t2
  print(' → {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  cont += 1
print(' → FIM')

