# desafio 095

# Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


jogador = dict()
galera = list()
soma = media = 0
while True:
  jogador.clear()
  jogador['nome'] = str(input('Nome do jogador: '))
  tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  for c in range(0, tot):
    gol = int(input(f'Quantos gols na partida {c}? '))
    jogador['gols'] = gol
    jogador['total'] = gol
    galera.append(jogador.copy())
  jogador.clear()
  while True:
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if resp == 'N':
    break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(galera):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-' * 40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(galera):
    print(f'ERRO! Não existe jogador com código {busca}!')
  else:
    print(f' -- LEVANTAMENTO DO JOGADOR {galera[busca]["nome"]}:')
    for i, g in enumerate(galera[busca]['gols']):
      print(f'    No jogo {i+1} fez {g} gols.')
  print('-' * 40)
print('<< VOLTE SEMPRE >>')
