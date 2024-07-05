# desaio 093

# crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantos gols ele marcou. No final, tudo isso sera guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['nome'] = str(input('digite o nome do jogador: '))
partidas = int(input('digite o total de partidas jogadas: '))

jogador['gols'] = []
jogador['total'] = 0
for c in range(0, partidas):
  gols = int(input('digite a quantidade de gols: '))
  jogador['gols'].append(gols)
  jogador['total'] += gols

print(jogador)

for k, v in jogador.items():
  print(f'{k} tem o valor {v}')
  
