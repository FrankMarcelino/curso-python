# desafio 027

# Faca um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente.

nome = str(input('digite seu nome: ')).strip().split()
print('seu primeiro nome e: {}'.format(nome[0]))
print('seu ultimo nome e: {}'.format(nome[len(nome)-1]))