# desafio 72

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte. Seu programa devera ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  num = int(input('Digite um número entre 0 e 20: '))
  if 0 <= num <= 20:
    break
  print('Tente novamente. ', end='')
print(f'Voce digitou o número {numero[num]}')


