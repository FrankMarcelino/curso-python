# desafio 056

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

from datetime import date
ano = date.today().year

maiorIdade = 0
qtdMulheres = 0

for c in range(1, 5):
  nome = input('digite o nome da {} pessoa: '.format(c))
  idade = int(input('digite a idade da {} pessoa: '.format(c)))
  sexo = input('digite o sexo da {} pessoa: '.format(c))

  if sexo == 'M' and idade > maiorIdade:
    maiorIdade = idade
    nomeMaiorIdade = nome

  if sexo == 'F' and idade < 20:
    qtdMulheres = qtdMulheres + 1

mediaIdade = (idade + idade + idade + idade) / 4

print('a media de idade do grupo e: {}'.format(mediaIdade))
print('o nome do homem mais velho e: {}'.format(nomeMaiorIdade))
print('a quantidade de mulheres com menos de 20 anos e: {}'.format(qtdMulheres))
