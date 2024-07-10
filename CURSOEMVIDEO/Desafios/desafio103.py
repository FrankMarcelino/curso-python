# desafio 103

# faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
  print(f'o jogador {jog} fez {gol} gol(s) no campeonato.') 

#programa principal
nome = str(input('nome do jogador: '))
gols = str(input('total de gols: '))
if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0
if nome.strip() == '':
  ficha(gol=gols)
else:
  ficha(nome, gols)


