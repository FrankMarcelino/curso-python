# desafio 100

# Crie um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep  

def sorteia():
  print('sorteando 5 valores da lista: ', end='')
  for c in range(0, 5):
    n = randint(0, 10)
    lista.append(n)
    print(f'{n} ', end='', flush=True)
    sleep(0.3)
  print('PRONTO!')
  
def somaPar():
  soma = 0
  for valor in lista:
    if valor % 2 == 0:
      soma += valor
  print(f'somando os valores pares de {lista}, temos {soma}')
  
lista = list()
sorteia()
somaPar()
