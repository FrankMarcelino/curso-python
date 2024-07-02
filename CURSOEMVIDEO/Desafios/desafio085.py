# desafio 085

# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica
# que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem
# crescente.

lista = [[], []]
valor = 0
for c in range(1, 8):
  valor = int(input('digite o {} valor: '.format(c)))
  if valor % 2 == 0:
    lista[0].append(valor)
  else:
    lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print('os valores pares digitados foram: {}'.format(lista[0]))
print('os valores impares digitados foram: {}'.format(lista[1]))

