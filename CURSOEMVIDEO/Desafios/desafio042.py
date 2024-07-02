# desafio 042

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isoceles: dois lados iguais
# - Escaleno: todos os lados diferentes

ladoA = float(input('digite o valor do primeiro lado: '))
ladoB = float(input('digite o valor do segundo lado: '))
ladoC = float(input('digite o valor do terceiro lado: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
  print('os valores informados formam um triangulo')

  if ladoA == ladoB == ladoC:
    print('triangulo equilatero')
  elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('triangulo isoceles')
  else:
    print('triangulo escaleno')
else:
  print('os valores informados nao formam um triangulo')

