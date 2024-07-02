# desafio 81

# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:

# A) Quantos valores foram digitados.

# B) A lista de valores ordenada de forma decrescente.

# C) Se o valor 5 foi digitado e esta ou nao na lista.


valores = []

while True:
  num = int(input('digite um valor: '))
  if num not in valores:
    valores.append(num)
    print('valor adicionado com sucesso')
  else:
    print('valor duplicado, tente novamente')
  resp = str(input('quer continuar? [S/N] '))
  if resp in 'Nn':
    break

print(f'os valores digitados foram: {valores}')
print(f'os valores em ordem decrescente foram: {sorted(valores, reverse=True)}')
print('o valor 5 faz parte da lista' if 5 in valores else 'o valor 5 nao faz parte da lista')