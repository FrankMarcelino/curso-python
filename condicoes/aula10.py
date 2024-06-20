# primeiro exemplo
nome = str(input('Qual seu nome? '))
if nome == 'Frank':
  print('Que nome lindo vc tem!')
else:
  print('Seu nome é legal')
print('Bom dia, {}'.format(nome))
print('--fim do primeiro exemplo--')

# segundo exemplo
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('sua media foi {:.1f}'.format(media))
if media >= 7:
  print('Voce foi aprovado! PARABENS!')
else:
  print('sua media foi ruim! ESTUDE MAIS!')
print('--fim do segundo exemplo--')