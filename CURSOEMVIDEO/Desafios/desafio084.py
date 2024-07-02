# desafio 084
# Crie um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

pessoas = list()
dados = list()
maiorPeso = menorPeso = 0

while True:
  dados.append(str(input('nome: ')))
  dados.append(float(input('peso: ')))
  if len(pessoas) == 0:
    maiorPeso = menorPeso = dados[1]
  else:
    if dados[1] > maiorPeso:
      maiorPeso = dados[1]
    if dados[1] < menorPeso:
      menorPeso = dados[1]
  pessoas.append(dados[:])
  dados.clear()
  resp = str(input('quer continuar? [S/N] '))
  if resp in 'Nn':
    break

print(f'foram cadastradas {len(pessoas)} pessoas')

print(f'a pessoa mais pesada foi: ', end='')
for p in pessoas:
  if p[1] == maiorPeso:
    print(f'{p[0]}', end=' ')

print(f'\na pessoa mais leve foi: ', end='')
for p in pessoas:
  if p[1] == menorPeso:
    print(f'{p[0]}', end=' ')
    
    
    