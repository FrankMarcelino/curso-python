# desafio 020
# O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('digite o nome do primeiro aluno: '))
aluno2 = str(input('digite o nome do segundo aluno: '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('digite o nome do terceiro aluno: '))

sortearOrdem = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(sortearOrdem)

print('a ordem de apresentação sera: {}'.format(sortearOrdem))

