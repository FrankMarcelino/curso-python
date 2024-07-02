# desafio 068
# Faca um programa que jogue par ou impar com o computador. O jogo so vai ser interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-' * 20)

vitorias = 0
while True:
  computador = randint(0, 10)
  jogador = int(input('Diga um valor: '))
  parImpar = ' '
  while parImpar not in 'PI':
    parImpar = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
  print('JO')
  sleep(1)
  print('KEN')
  sleep(1)
  print('PO!!!')
  sleep(1)
  print('-' * 20)
  soma = computador + jogador
  if parImpar == 'P':
    if soma % 2 == 0:
      print('Voce venceu!')
      vitorias += 1 
    else:
      print('Voce perdeu!')
      break
  elif parImpar == 'I':
    if soma % 2 == 1:
      print('Voce venceu!')
      vitorias += 1
    else:
      print('Voce perdeu!')
      break
  print('Vamos jogar novamente...')
print('GAME OVER! Voce venceu {} vezes'.format(vitorias))
