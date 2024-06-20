# desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.  

salario = float(input('digite o valor do seu salario: '))

if salario > 1250:
  aumento = (salario * 0.10) + salario
else:
  aumento = (salario * 0.15) + salario

print('o valor do seu novo salario e: {}'.format(aumento))
