# desafio 26

# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece a ultima vez

frase = str(input('digite uma frase: ')).strip().upper()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na posicao {}'.format(frase.find('A')+1))
print('a letra A aparece pela ultima vez na posicao {}'.format(frase.rfind('A')+1))