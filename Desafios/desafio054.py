# desafio 054

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
  nasc = int(input('ano de nascimento da {} pessoa: '.format(pessoa)))
  idade = atual - nasc
  if idade >= 21:
    totmaior += 1
  else:
    totmenor += 1
print('ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e {} pessoas menores de idade'.format(totmenor))
