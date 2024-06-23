# desafio 048

# Faca um programa que calcule a soma entre todos os numeros impares e que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.

soma = 0

for c in range(1, 501, 2):
  if c % 3 == 0:
    soma = soma + c   

print('a soma de todos os valores que são multiplos de 3 se encontram entre 1 e 500 é: {}'.format(soma))

