# aula 21

def fatorial(n):
  f = 1
  for c in range(n, 0, -1):
    f *= c
  return f

n = int(input('digite um numero: '))
print(fatorial(n))