def aumentar(preco=0, porcentagem=0, formatado=False):
  res = preco + (preco * porcentagem / 100)
  return res if formatado is False else moeda(res)
  
def diminuir(preco=0, porcentagem=0, formatado=False):
  res = preco - (preco * porcentagem / 100)
  return res if formatado is False else moeda(res)
  
def dobrar(preco=0, formatado=False):
  res = preco * 2
  return res if formatado is False else moeda(res)
  
def metade(preco=0):
  print(f'A metade de {preco} fica {preco / 2}.')
  
def moeda(preco=0, moeda='R$'):
  return f'{moeda}{preco:.2f}'.replace('.', ',')

