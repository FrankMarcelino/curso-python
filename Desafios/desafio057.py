# desafio 057

# Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente ate ter um valor correto.

sexo = str(input('digite o seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
  print('\33[31m Valor invalido, tente novamente')
  sexo = str(input('digite o seu sexo: [M/F] ')).strip().upper()[0]

print('\33[32m sexo {} registrado com sucesso'.format(sexo))