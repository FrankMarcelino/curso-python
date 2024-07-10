# desafio 102

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que vai mostrar a progressão


from time import sleep

def fatorial(n, show=False):
  """
  -> Calcula o fatorial de um número
  :param n: o número a ser calculado
  :param show: (opcional) mostrar ou não a conta
  :return: o valor do fatorial de um número n
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f

# programa principal
n = int(input('digite um número: '))
print(fatorial(n, show=False))



