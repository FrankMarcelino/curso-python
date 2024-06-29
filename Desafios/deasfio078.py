# desafio 078

# Faca um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.

valores = []

for c in range(0, 5):
  valores.append(int(input('digite um valor: ')))

print('o maior valor digitado foi: {} e sua posicao foi: {}'.format(max(valores), valores.index(max(valores))))
print('o menor valor digitado foi: {} e sua posicao foi: {}'.format(min(valores), valores.index(min(valores))))
