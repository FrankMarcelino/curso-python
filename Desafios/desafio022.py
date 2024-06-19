# desafio 022

# Faca um programa que leia o nome completo de uma pessoa
# Mostre o nome com todas as letras maiusculas
# Mostre o nome com todas as letras minusculas
# Quantas letras ao todo(sem considerar espacos)
# Quantas letras no primeiro nome

nome = str(input('digite seu nome: ').strip())

print('seu nome em maiusculas e: {}'.format(nome.upper()))
print('seu nome em minusculas e: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))