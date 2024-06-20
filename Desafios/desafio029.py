# desafio 029

# Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do seu carro? '))

if velocidade > 80:
  print('MULTADO! Voce excedeu o limite permitido que e de 80km/h')
  print('Voce deve pagar uma multa de R${:.2f}'.format((velocidade - 80) * 7))
else:
  print('Tenha um bom dia! Dirija com segurança!')

