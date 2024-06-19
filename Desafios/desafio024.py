# desafio 024

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"

nome = str(input('digite o nome da sua cidade: ')).strip().title()  
primeiroNome = nome.split()[0]

comecaComSanto = 'Santo' in primeiroNome

print('sua cidade começa com Santo? {}'.format(comecaComSanto))
3