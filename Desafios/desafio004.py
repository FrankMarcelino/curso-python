#desafio 04

algoFoiDgitado = input('digite algo: ')

print('O tipo primitivo desse valor e: ', type(algoFoiDgitado))
print('So tem espaços? ', algoFoiDgitado.isspace())
print('E um numero? ', algoFoiDgitado.isnumeric())
print('E alfabetico? ', algoFoiDgitado.isalpha())
print('E alfanumerico? ', algoFoiDgitado.isalnum())
print('Esta em maisculas? ', algoFoiDgitado.isupper())
print('Esta em minusculas? ', algoFoiDgitado.islower())
print('Esta capitalizada? ', algoFoiDgitado.istitle())