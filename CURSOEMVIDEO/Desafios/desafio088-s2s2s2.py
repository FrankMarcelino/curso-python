# desafio 088

# Faca um programa que ajude um jogador da mega sena. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
from operator import itemgetter
jogos = []
print('-' * 30)
print('     JOGA NA MEGA SENA    ')
print('-' * 30)
jogos = list()
for c in range(0, 6):
  jogos.append([])
  for i in range(0, 6):
    jogos[c].append(randint(1, 60))
  jogos[c].sort()
  sleep(1)
  print(f'Jogo {c+1}: {jogos[c]}')
  sleep(1)
print('-=' * 3, f'{"BOA SORTE":^15}', '-=' * 3)

