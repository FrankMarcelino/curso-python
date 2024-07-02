
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
  print(f'Eu iria comer {comida}') 
  
for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posicao {pos}')

print('Comi pra caramba!')