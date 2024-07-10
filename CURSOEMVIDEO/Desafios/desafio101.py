# desafio 101

#crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto obrigatorio ou nao

from datetime import date 
ano = int(input('digite o ano de nascimento: '))

idade = date.today().year - ano

def voto(idade):
  if idade < 16:
    print('nao vota')
  elif 16 <= idade < 18 or idade > 65:
    print('voto opcional')
  else:
    print('voto obrigatorio')

voto(idade)

