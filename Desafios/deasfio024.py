# desafio 024

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"

nome = str(input('digite o nome da sua cidade: ')).strip().title()  

repostaSantoInName = 'Santo' in nome

print('sua cidade começa com Santo? {}'.format(repostaSantoInName))
