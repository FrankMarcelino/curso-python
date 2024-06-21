# desafio 043

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 ate 30: Sobrepeso
# - 30 ate 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('digite o seu peso: '))
altura = float(input('digite a sua altura: '))

imc = peso / (altura * altura)

print('seu imc e: {}'.format(imc))

if imc < 18.5:
  print('abaixo do peso')
elif imc >= 18.5 and imc <= 25:
  print('peso ideal')
elif imc > 25 and imc <= 30:
  print('sobrepeso')
elif imc > 30 and imc <= 40:
  print('obesidade')
else:
  print('obesidade morbida')

  