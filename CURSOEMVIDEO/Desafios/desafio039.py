# desafio 039

# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua categoria, de acordo com sua idade: se ele ainda vai se alistar, se e a hora de se alistar, se ja passou do tempo do alistamento.

from datetime import date
ano = int(input('digite o ano de nascimento: '))

idade = date.today().year - ano

print('sua idade e de {} anos'.format(idade)) 

if idade < 18:
  print('ainda faltam {} anos para o alistamento'.format(18 - idade))
  print('seu alistamento sera em {}'.format(ano + 18))
elif idade == 18:
  print('este ano e o seu alistamento')
elif idade > 18:
  print('ja passou do tempo do alistamento')