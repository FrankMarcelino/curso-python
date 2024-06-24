# desafio 058

# faça um programa que pense em um numero  entre 0 e 10 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu. E jogo rodara até o usurio acertar.


from random import randint
from time import sleep

computador = randint(1, 2)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

palpite = 0
while palpite != computador:
  palpite = int(input('\n Em que numero eu pensei? '))
  print('PROCESSANDO...')
  sleep(3)
  if palpite == computador:
    print('\33[32m PARABENS! Voce acertou!')
  else:
    print('\33[33m GANHEI! Eu pensei o {} e nao o {}'.format(computador, palpite))
    