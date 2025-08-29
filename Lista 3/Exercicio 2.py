## Exercicio 2 lista 3
## Solicite dois números e verifique se pelo menos um deles é múltiplo de 5.
numero = int(input('Informe um Numero:'))
numero2 = int(input('Informe outro'))
if numero % 5 == 0 or numero2  % 5 == 0:
  print('Correto! Pelo menos um dos números informados é múltiplo de 5.')
else:
  print('Nenhum dos números informados é múltiplo de 5.')