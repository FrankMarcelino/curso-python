# desafio 094

# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas
# b) a media de idade
# c) uma lista com todoso menores
# d) uma lista com todas as peossoas com idade acima da media

dicionario = list()
pessoa = dict()
soma = 0
media = 0
maior = list()
menor = list()
while True:
  pessoa['nome'] = str(input('digite o nome: '))
  pessoa['sexo'] = str(input('digite o sexo [M/F]: ')).upper()[0]
  pessoa['idade'] = int(input('digite a idade: '))
  soma += pessoa['idade']
  dicionario.append(pessoa.copy())
  pessoa.clear()
  resp = str(input('quer continuar? [S/N] '))
  if resp in 'Nn':
    break
  

print(dicionario)
print(f'foram cadastradas {len(dicionario)} pessoas')
media = soma / len(dicionario)
print(f'a media de idade e de {media} anos')
print(f'as pessoas com idade acima da media sao: ')
for p in dicionario:
  if p['idade'] > media:
    print(f'{p["nome"]}')
  else:
    print(f'{p["nome"]}')

