# desafio 041

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - Ate 9 anos: MIRIM
# - Ate 14 anos: INFANTIL
# - Ate 19 anos: JUNIOR
# - Ate 25 anos: SENIOR
# - Acima de 25 anos: MASTER

from datetime import date
ano = int(input('digite o ano de nascimento: '))

idade = date.today().year - ano

print('sua idade e de {} anos'.format(idade))

if idade <= 9:
  print('sua categoria e MIRIM')
elif idade <= 14:
  print('sua categoria e INFANTIL')
elif idade <= 19:
  print('sua categoria e JUNIOR')
elif idade <= 25:
  print('sua categoria e SENIOR')
else:
  print('sua categoria e MASTER')