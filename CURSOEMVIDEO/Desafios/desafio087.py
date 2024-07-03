# desafio 087
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terça coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
maiorValorSegundaLinha = 0
somaTerceiraColuna = 0
print('digite os valores da matriz:')

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
  for c in range(0, 3):
    if matriz[l][c] % 2 == 0:
      somaPar += matriz[l][c]
    if c == 2:
      somaTerceiraColuna += matriz[l][c]
    if l == 1:
      if maiorValorSegundaLinha < matriz[l][c]:
        maiorValorSegundaLinha = matriz[l][c]
        
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()

print()
print()
print()
print('a matriz digitada e:')

print('a soma de todos os valores pares digitados e: {}'.format(somaPar))
print('a soma dos valores da terça coluna e: {}'.format(somaTerceiraColuna))
print('o maior valor da segunda linha e: {}'.format(maiorValorSegundaLinha))

      
      
      
      