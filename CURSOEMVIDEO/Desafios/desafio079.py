# desafio 079

#crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele não sera adicionado. No final, serão exibidos todos os valores unicos digitados, em ordem crescente.

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
valores.sort()
print(f'os valores digitados foram {valores}')
