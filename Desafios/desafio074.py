# desafio 074
# crie uma program que vai gerar 5 numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
  print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)} e o menor foi {min(numeros)}')  

