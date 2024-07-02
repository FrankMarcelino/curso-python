# desafio 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se o usuário quer ou não continuar a digitar valores.

numeros = []
media = 0
maiorValor = 0
menorValor = 0

while True:
  numeros.append(int(input('digite um numero: ')))
  media = sum(numeros) / len(numeros)
  maiorValor = max(numeros)
  menorValor = min(numeros)
  continuar = str(input('deseja continuar? [S/N] ')).strip().upper()[0]
  if 'N' in continuar:
    break

print('a media dos valores digitados e: {}'.format(media))
print('o maior valor e: {}'.format(maiorValor))
print('o menor valor e: {}'.format(menorValor))


  

  