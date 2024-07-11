def aumentar(preco=0, porcentagem=0, formatado=False):
  res = preco + (preco * porcentagem / 100)
  return res if formatado is False else moeda(res)
  
def diminuir(preco=0, porcentagem=0, formatado=False):
  res = preco - (preco * porcentagem / 100)
  return res if formatado is False else moeda(res)
  
def dobrar(preco=0, formatado=False):
  res = preco * 2
  return res if formatado is False else moeda(res)
  
def metade(preco=0, formatado=False):
  res = preco / 2
  return res if formatado is False else moeda(res)
  
def moeda(preco=0, moeda='R$'):
  return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, aumento=0, redução=0):
  print('-' * 30)
  print('RESUMO DO VALOR'.center(30))
  print('-' * 30)
  print(f'{"Preço analisado:":<20} {moeda(preco)}')
  print(f'{"Dobro do preço:":<20} {dobrar(preco, True)}')
  print(f'{"Metade do preço:":<20} {metade(preco, True)}')
  print(f'{f"{aumento}% de aumento":<20} {aumentar(preco, aumento, True)}')
  print(f'{f"{redução}% de redução":<20} {diminuir(preco, redução, True)}')
  print('-' * 30)