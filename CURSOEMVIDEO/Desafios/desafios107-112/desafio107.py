from utilidade.moeda import utilidadePreco

print('-' * 30)
print('{:^30}'.format('verficador de preço'))
print('-' * 30)
print('MENU PRINCIPAL')
print('-' * 30)
print('[1] - Aumentar')
print('[2] - Diminuir')
print('[3] - Dobrar')
print('[4] - Metade')
print('[5] - Sair')
print('-' * 30)
preco = float(input('Digite o preço: R$'))

while True:
  print('-' * 30)
  opcao = int(input('Qual a sua opção? '))
  if opcao == 1:
    porcentagem = int(input('Qual a porcentagem? '))
    print(utilidadePreco.aumentar(preco, porcentagem, True))
  elif opcao == 2:
    porcentagem = int(input('Qual a porcentagem? '))
    print(utilidadePreco.diminuir(preco, porcentagem, True))
  elif opcao == 3:
    print(utilidadePreco.dobrar(preco, True))
  elif opcao == 4:
    print(utilidadePreco.metade(preco, True))
  elif opcao == 5:
    break
  else:
    print('Opção inválida, tente novamente!')
  print('-' * 30)
  print('MENU PRINCIPAL')
  print('-' * 30)
  print('[1] - Aumentar')
  print('[2] - Diminuir')
  print('[3] - Dobrar')
  print('[4] - Metade')
  print('[5] - Sair')
  print('-' * 30)
  preco = float(input('Digite o preço: R$'))