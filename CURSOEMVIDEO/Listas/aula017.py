# aula 17

# lista 
listaNomes = []
while True:
  print('-' * 30)
  print('MENU PRINCIPAL')
  print('-' * 30)
  print('[1] - Cadastrar')
  print('[2] - Consultar')
  print('[3] - Excluir')
  print('[4] - Sair')
  print('-' * 30)
  
  op = int(input('escolha uma opção: '))

  if op == 1:
    listaNomes.append(input('digite o nome: '))
    print('Cadastrando...')
  

  elif op == 2:
    print('Consultando...')
    for nome in listaNomes:
      print('{}'.format(nome))
      
 

  elif op == 3:
    print('lista de nomes e: {}'.format(listaNomes))
    listaNomes.remove(input('digite o nome: '))
    print('Excluindo...')
    

  elif op == 4:
    print('Saindo...')
    break

  else:
    print('opção invalida, tente novamente!')
    
  