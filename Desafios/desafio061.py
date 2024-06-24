# desafio 061

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))

termo = primeiroTermo
cont = 1
while cont <= 10:
  print('{} -> '.format(termo), end='')
  termo += razao
  cont += 1
print('fim')