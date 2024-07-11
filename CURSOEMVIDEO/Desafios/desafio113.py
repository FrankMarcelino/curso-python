# desafio 113

# reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
      continue
    except KeyboardInterrupt:
      print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
      return 0
    else:
      return n
    
    
def leiaFloat(msg):
  while True:
    try:
      n = float(input(msg))
    except (ValueError, TypeError):
      print('\033[31mERRO: por favor, digite um número real válido.\033[m')
      continue
    except KeyboardInterrupt:
      print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
      return 0
    else:
      return n
    
    
n = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'Você digitou o número inteiro {n} e o real {f}')
    