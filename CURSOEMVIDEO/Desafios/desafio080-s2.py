# desafio 080

# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []

for c in range(0, 5):
  num = int(input('digite um valor: '))
  if c == 0 or num > numeros[-1]:
    numeros.append(num)
  else:
    pos = 0
    while pos < len(numeros):
      if num <= numeros[pos]:
        break
      pos += 1
    numeros.insert(pos, num)
print(numeros)