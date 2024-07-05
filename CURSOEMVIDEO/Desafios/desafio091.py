# desafio 091

#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
print('valores sorteados: ')
for k, v in jogadores.items():
  print(f'{k} tirou {v} no dado.')
  sleep(1)
  