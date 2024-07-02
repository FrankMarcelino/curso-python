# desafio 082

# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:

#Crie duas listas extras que vaao conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final mostre o conteudo das 3 listas geradas.

numeros = []
pares = []
impares = []

while True:
  num = int(input('digite um valor: '))
  numeros.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  resp = str(input('quer continuar? [S/N] '))
  if resp in 'Nn':
    break
print('-=' * 30)
print(f'os valores digitados foram: {numeros}')
print(f'os valores pares digitados foram: {pares}')
print(f'os valores impares digitados foram: {impares}')