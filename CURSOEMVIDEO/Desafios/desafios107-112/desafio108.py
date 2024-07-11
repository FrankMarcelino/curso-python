# desafio 108

# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import utidadesPreco

preco = float(input('digite o preço: R$'))
print('preço formatado: {}'.format(utidadesPreco.moeda(preco)))
