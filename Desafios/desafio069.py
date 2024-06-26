# desafio 069
# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

soma = 0
mulheres = 0
homens = 0

while True:
  idade = int(input('digite sua idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
  if idade >= 18:
    soma += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres += 1
  resp = ' '
  while resp not in 'SN':
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
  if resp == 'N':
    break
print('existem {} pessoas maiores de 18 anos'.format(soma))
print('existem {} homens'.format(homens))
print('existem {} mulheres menores de 20 anos'.format(mulheres))

