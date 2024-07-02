# desafio 73
# crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Vasco.

classificacaoSerieA2024 = ("flamengo", "bahia","botafogo","palmeiras","cruzeiro", "athletico-PR","são paulo","bragantino","internacional","atletico-MG","fortaleza","juventude","criciuma","EC vitoria","vasco","atletico-GO","corintians","gremio","fluminense")

while True:
  print('\033[31m{}'.format('CLASSIFICAÇÃO SÉRIE A 2024'))
  print('1 - Primeiros colocados\n2 - Últimos colocados\n3 - Times em ordem alfabética\n4 - Em que posição está o time da Vasco\n0 - Sair')
  opcao = int(input('digite sua escolha: '))

  if opcao == 1:
    print("\033[32m{}".format(classificacaoSerieA2024[0:5]))

  elif opcao == 2:
    print("\033[33m{}".format(classificacaoSerieA2024[16:20]))

  elif opcao == 3:
    print("\033[34m{}".format(sorted(classificacaoSerieA2024)))

  elif opcao == 4:
    print("\033[35m posição do time Vasco no campeonato é: {}".format(classificacaoSerieA2024.index('vasco')+1))

  elif opcao == 0:
    print("\033[36m{}".format('FIM do programa'))
    break