# desafio 104

# Crie um programa que tenha a função leaint() que vai funcionar de forma semelhante a função input() do Python, sendo que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leaint('Digite um n')

def leaint(msg):
  ok = False
  valor = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
    if ok:
      break
  return valor

n = leaint('digite um numero: ')
