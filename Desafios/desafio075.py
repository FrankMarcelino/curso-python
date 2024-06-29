# desafio 075

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

numeros = (int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')))

print('O nove apareceu {} vezes'.format(numeros.count(9)))
print('o primeiro nove foi digitado na posição {}'.format(numeros.index(3) + 1))
print('os pares digitados foram: ', end='')
for n in numeros:
  if n % 2 == 0:
    print(n, end=' ')


    

