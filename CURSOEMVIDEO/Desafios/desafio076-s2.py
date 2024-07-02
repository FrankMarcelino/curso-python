# desafio 076

# crie um programa que tenha uma tupppla unica com nomes de produtos e seus respectivos precos, na sequencia. No final, mostre uma listagem de precos, organizando os dados em forma tabular.

from time import sleep
from operator import itemgetter

print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

listagem = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)

for pos in range(0, len(listagem)):
  if pos % 2 == 0:
    print(f'{listagem[pos]:.<30}', end='')
  else:
    print(f'R${listagem[pos]:>7.2f}')
  sleep(0.5)

print('-' * 30)


