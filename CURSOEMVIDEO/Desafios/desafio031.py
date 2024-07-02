# desafio 031

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de ate 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))

if distancia <= 200:
  print('O valor da sua passagem e de: R${:.2f}'.format(distancia * 0.50))
else:
  print('O valor da sua passagem e de: R${:.2f}'.format(distancia * 0.45))
  