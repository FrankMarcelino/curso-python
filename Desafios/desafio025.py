# desafio 025

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('digite o nome da pessoa: ')).strip().title()

repostaSilvaInName = 'Silva' in nome

print('o nome tem silva? {}'.format(repostaSilvaInName))