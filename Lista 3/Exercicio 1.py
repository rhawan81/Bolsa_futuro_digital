## Exercicio 1 lista 3
## Peça a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos (inclusive).

idade = int(input('Informe sua idade : '))
if idade >= 18 and idade <= 30:
 print('Correto! Sua idade está entre 18 e 30 anos.')
else:
  print('Sua idade está fora do intervalo de 18 a 30 anos.')