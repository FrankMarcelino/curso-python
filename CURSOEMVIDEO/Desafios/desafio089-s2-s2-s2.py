# desafio 089
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada um individualmente.

# obs: o programa vai mostrar quantas pessoas foram cadastradas, a media de cada um, a maior e a menor nota lida.

input('''
digite 0 para encerrar o programa ou tecla ENTER para continuar:
''')

cadastro = list()
aluno = list()

while True:
  nome = str(input('digite o nome do aluno: '))

  if nome == '0':
    break

  nota1 = float(input('digite a primeira nota: '))
  nota2 = float(input('digite a segunda nota: '))

  media = (nota1 + nota2) / 2

  cadastro.append([nome, [nota1, nota2], media])

print('-=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(cadastro):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('-' * 30)
input('digite 0 para encerrar o programa ou tecla ENTER para continuar: ')

while True:
  print('-' * 30)
  opcao = int(input('mostrar as notas de qual aluno? (999 interrompe): '))
  if opcao == 999:
    print('finalizando...')
    break
  if opcao <= len(cadastro) - 1:
    print(f'as notas de {cadastro[opcao][0]} sao {cadastro[opcao][1]}')
  else:
    print('opcao invalida, tente novamente!')
    



