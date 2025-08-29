## Exercicio 5 lista 4
## Peça um número e exiba sua tabuada de 1 a 10.
user = int(input('Informe seu numero:'))
for i in range(0,11):
  print(f'{user} x {i} = {user * i}')