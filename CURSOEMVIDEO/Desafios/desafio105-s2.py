# desafio 105

# Faca um programa que tenha uma funcao chamada notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes:

# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situacao (opcional)

# Adicione tambem as docstrings da funcao.

def notas(*n, sit=False):
  """
  -> Funcao para analisar notas e situacao de varios alunos.
  :param n: uma ou mais notas dos alunos (aceita varias)
  :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
  :return: dicionario com varias informacoes da turma
  """
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n)/len(n)
  if sit:
    if r['media'] >= 7:
      r['situacao'] = 'BOA'
    elif r['media'] >= 5:
      r['situacao'] = 'Razoável'
    else:
      r['situacao'] = 'Ruim'
  return r


n = float(input('digite a primeira nota: '))
m = float(input('digite a segunda nota: '))
n2 = float(input('digite a terceira nota: '))
n3 = float(input('digite a quarta nota: '))

resp = notas(n, m, n2, n3, sit=True)

print(resp)
