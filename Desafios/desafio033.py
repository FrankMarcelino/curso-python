# desafio 033

# Faca um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

maior = n1
menor = n1

if n2 > maior:
  maior = n2
if n3 > maior:
  maior = n3

if n2 < menor:
  menor = n2  
if n3 < menor:
  menor = n3

print('o maior valor digitado foi {}'.format(maior))
print('o menor valor digitado foi {}'.format(menor))