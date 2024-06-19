# desafio 023

# Faca um programa que leia um numero de 0 a 9999
# e mostre na tela cada um dos digitos separados

numero = int(input('digite um numero de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))