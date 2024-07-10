# desafio 106

# faça um minisistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrara. Importante: use cores.

from time import sleep
c = ('\033[m',          # 0 sem cores
  '\033[0;30;41m',   # 1 vermelho
  '\033[0;30;42m',   # 2 verde
  '\033[0;30;43m',   # 3 amarelo
  '\033[0;30;44m',   # 4 azul
  '\033[0;30;45m',   # 5 roxo
)

def ajuda(com):
  ti = f'{c[4]}COMANDO \'{com}\'{c[0]}'
  print(c[3], end='')
  help(com)
  print(c[0], end='')
  sleep(1)
  
def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(c[cor], end='')
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)
  print(c[0], end='')
  sleep(1)
  
comando = ''
while True:
  titulo('SISTEMA DE AJUDA PyHELP', 2)
  comando = str(input('Função ou Biblioteca > '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
    
print(c[4], end='')
print('Até logo!')
print(c[0], end='')

  
