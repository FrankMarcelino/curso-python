# desafio 062

# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))

termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while cont <= total:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
  print('pau')
  mais = int(input('quantos termos voce quer mostrar a mais? '))

print('fim')