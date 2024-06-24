# desafio 055

# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
  peso = float(input('digite o peso da {} pessoa: '.format(c)))
  if c == 1:
    maiorPeso = peso
    menorPeso = peso
  else:
    if peso > maiorPeso:
      maiorPeso = peso
    if peso < menorPeso:
      menorPeso = peso

print('o maior peso lido foi: {}'.format(maiorPeso))
print('o menor peso lido foi: {}'.format(menorPeso))
