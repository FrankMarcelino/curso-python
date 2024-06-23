# deafio 046

# Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, com uma pausa de 1 segundo entre eles.


from time import sleep
for c in range(10, -1, -1):
  print(c)  
  sleep(1)
print('BOOM!')

