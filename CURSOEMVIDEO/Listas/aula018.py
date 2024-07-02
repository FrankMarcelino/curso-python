# aula 18

# lista compostas 

galera = list()
dado = list()
while True:
  dado.append(str(input('nome: ')))
  dado.append(float(input('peso: ')))
  galera.append(dado[:])
  dado.clear()
  resp = str(input('quer continuar? [S/N] '))
  if resp in 'Nn':
    break
print(galera)
print(f'foram cadastrados {len(galera)} pessoas')
