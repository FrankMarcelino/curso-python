# tratamento de erros

try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  r = a / b
except (ValueError, TypeError):
  print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
  print('Não é possivel dividir um numero por zero.')
except KeyboardInterrupt:
  print('O usuario preferiu não informar os dados.')
except Exception as erro:
  print(f'O erro encontrado foi {erro.__class__}')
else:
  print(f'O resultado e {r:.1f}')
finally:
  print('Volte sempre! Muito obrigado!')