# desafio 092

# crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário recebera também o ano de contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
from time import sleep
from operator import itemgetter
cadastro = dict()
cadastro['nome'] = str(input('digite o nome: '))
nasc = int(input('digite o ano de nascimento: '))
cadastro['idade'] = date.today().year - nasc
cadastro['ctps'] = int(input('digite o ctps (0 para nao tem): '))

print('carregando dados...')
sleep(1)

if cadastro['ctps'] != 0:
  cadastro['contratacao'] = int(input('digite o ano de contratacao: '))
  cadastro['salario'] = float(input('digite o salario: '))
  cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['contratacao'] + 35) - date.today().year
  print(cadastro)
else:
  print(cadastro)

for k, v in cadastro.items():
  print(f'{k} tem o valor {v}')
  