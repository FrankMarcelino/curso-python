# desafio 107

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco=0, porcentagem=0):
  print(f'R${preco} com {porcentagem}% de aumento fica R${(preco * (1 + (porcentagem / 100)))}.')
  
def diminuir(preco=0, porcentagem=0):
  print(f'R${preco} com {porcentagem}% de redução fica R${(preco * (1 - (porcentagem / 100)))}.')
  
def dobrar(preco=0):
  print(f'O dobro de R${preco} fica R${preco * 2}.') 

def metade(preco=0):
  print(f'A metade de R${preco} fica R${preco / 2}.')
  
def moeda(preco=0, moeda='R$'):
  return f'{moeda}{preco:.2f}'.replace('.', ',')