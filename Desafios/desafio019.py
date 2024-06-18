# desafio 019

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = str(input('digite o nome do primeiro aluno: '))
aluno2 = str(input('digite o nome do segundo aluno: '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('digite o nome do terceiro aluno: '))

print('o aluno escolhido foi: {}'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
