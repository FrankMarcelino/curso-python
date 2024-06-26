# desafio 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa devera perguntar se o usuário vai continuar. No final, mostre:
# A) qual e o total gasto na compra
# B) quantos produtos custam mais de R$1000
# C) qual e o nome do produto mais barato

total = 0
mais = 0
menor = 0
barato = ' '

while True:
  nome = str(input('digite o nome do produto: '))
  preço = float(input('digite o preço do produto: '))
  total += preço
  if preço > 1000:
    mais += 1
  if menor == 0 or preço < menor:
    menor = preço
    barato = nome
  resp = ' '
  while resp not in 'SN':
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
  if resp == 'N':
    break

print('o total da compra foi: {}'.format(total))
print('quantos produtos custam mais de R$1000: {}'.format(mais))
print('o nome do produto mais barato e: {}'.format(barato))

