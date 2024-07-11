# desafio 115

# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e mostrar todas as pessoas cadastradas.

# OBS: Cadastrando uma nova pessoa, não esquecer de adicionar o nome e a idade na primeira linha do arquivo.

while True:
  print('-' * 30)
  print('CADASTRO DE PESSOAS')
  print('-' * 30)
  print('[ 1 ] - CADASTRAR PESSOA')
  print('[ 2 ] - MOSTRAR PESSOAS CADASTRADAS')
  print('[ 3 ] - SAIR DO PROGRAMA')
  print('-' * 30)
  op = int(input('Qual sua opção? '))
  if op == 1:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    with open('cadastro.txt', 'a') as arquivo:
      arquivo.write(f'{nome};{idade}\n')
  elif op == 2:
    with open('cadastro.txt', 'r') as arquivo:
      for linha in arquivo:
        nome, idade = linha.strip().split(';')
        print(f'Nome: {nome} Idade: {idade}')
  elif op == 3:
    break
  else:
    print('Opção inválida! Tente novamente.')
  print('-' * 30)
