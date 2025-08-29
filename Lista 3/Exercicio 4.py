## Exercicio 4 lista 3
##  Peça um número inteiro e verifique se ele é par e positivo.

numero  = int(input('INforme um numero:'))
if numero % 2 == 0 and numero > 0:
  print('NUMERO PAR E POSITIVO')
else:
  print(f'O número {numero} não atende a ambos os critérios (ser par E positivo).')