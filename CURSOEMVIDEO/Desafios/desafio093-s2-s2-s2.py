# desaio 093

# crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantos gols ele marcou. No final, tudo isso sera guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['nome'] = str(input('digite o nome do jogador: '))
partidas = int(input('digite o total de partidas jogadas: '))

jogador['gols'] = []
jogador['total'] = 0
for c in range(0, partidas):
  gols = int(input('digite a quantidade de gols na partida {}: ' .format(c+1)))
  jogador['gols'].append(gols)
  jogador['total'] += gols

print('-=' * 30)
print(jogador)
print('-=' * 30)
print('e fez a media de {} gols por partida.'.format(jogador['total']/len(jogador['gols'])))
print('fez o total de {} gols'.format(jogador['total']))
print('-=' * 30)
print('o jogador {} jogou {} partidas.'.format(jogador['nome'], len(jogador['gols'])))
for k, v in enumerate(jogador['gols']):
  print('=> Na partida {} ele fez {} gols.' .format(k+1, v))
  

