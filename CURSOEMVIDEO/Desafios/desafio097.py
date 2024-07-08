# desafio 097

# crie um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adapta-vel.

def escreva(msg):
  print('-' * len(msg))
  print(msg)
  print('-' * len(msg))


escreva(str(input('digite um texto: ')))