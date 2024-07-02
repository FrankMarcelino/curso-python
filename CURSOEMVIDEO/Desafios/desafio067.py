# desafio 067
# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario
# O programa sera interrompido quando o numero solicitado for negativo

while True:
  print('digite um numero negativo para parar o programa')
  num = int(input('digite um numero: '))
  
  if num < 0:
    print('programa encerrado')
    break
  for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))