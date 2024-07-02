# desafio 075

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

numeros = (int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')))

if 9 in numeros:
  print('o valor 9 apareceu {} vezes'.format(numeros.count(9)))

else:
  print('o valor 9 nao foi digitado')

if 3 in numeros:  
  print('o valor 3 apareceu na {}° posição'.format(numeros.index(3) + 1))
else:
  print('o valor 3 nao foi digitado')  

for c in numeros:
  if c % 2 == 0:
    print('os valores pares digitados foram: {}'.format(c))
  

    



