# desafio 090

# faca um programa que nome e media de um aulono, guardando também a situação em um dicionário. No final, mostre o conteudo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('digite o nome do aluno: '))
aluno['media'] = float(input('digite a media do aluno: '))
aluno['situacao'] = 'aprovado' if aluno['media'] >= 7 else 'reprovado'

print('o nome do aluno é: {}'.format(aluno['nome']))
print('a media do aluno é: {}'.format(aluno['media']))
print('a situacao do aluno é: {}'.format(aluno['situacao']))