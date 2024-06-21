# desafio 040

# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:

# - media abaixo de 5.0: REPROVADO
# - media entre 5.0 e 6.9: RECUPERACAO
# - media 7.0 ou superior: APROVADO

nota01 = float(input('digite a primeira nota: '))
nota02 = float(input('digite a segunda nota: '))

media = (nota01 + nota02) / 2

print('a media entre {} e {} vale {}'.format(nota01, nota02, media))

if media < 5.0:
  print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
  print('RECUPERACAO')
else:
  print('APROVADO')

