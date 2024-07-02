# desafio 83

# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu aplicativo devera analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.

exp = str(input('digite uma expressão: '))

pilha = []
for simb in exp:
  if simb == '(':
    pilha.append('(')

  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()

    else: 
      pilha.append(')')
      break
    
if len(pilha) == 0:
  print('expressão valida')

else:
  print('expressão invalida')
  
  