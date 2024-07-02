# desafio 037

# escreva um program que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 1 para binario, 2 para octal e 3 para hexadecimal

numero = int(input('digite um numero: '))

print('''escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('sua opção: '))

if opcao == 1:
  print('{} convertido para BINARIO e igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
  print('{} convertido para OCTAL e igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
  print('{} convertido para HEXADECIMAL e igual a {}'.format(numero, hex(numero)[2:]))
else:
  print('opção invalida, tente novamente!')

  