def fatorial(num):
  f = 1
  for c in range(num, 0, -1):
    f *= c
  return f


num = int(input('digite um numero: '))
fat = fatorial(num)
print(f'o fatorial de {num} e: {fat}')
