# desafio 114

# teste de acesso ao site https://www.pudim.com.br

try:
  from urllib.request import urlopen
  site = urlopen('https://www.pudim.com.br')
except:
  print('O site pudim não esta acessível no momento.')
else:
  print('Consegui acessar o site Pudim com sucesso!')
  
