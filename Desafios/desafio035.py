# desafio 035

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

retaA = float(input('digite o valor da primeira reta: '))
retaB = float(input('digite o valor da segunda reta: '))
retaC = float(input('digite o valor da terceira reta: '))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
  print('as retas formam um triangulo')
else:
  print('as retas nao formam um triangulo')


  