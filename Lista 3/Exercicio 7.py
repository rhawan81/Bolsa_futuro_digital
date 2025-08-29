## Exercicio 7 lista 3
## Solicite três números e verifique se pelo menos dois deles são iguais.
numero1 = int(input('Informe um numero : '))
numero2 = int(input('Informe um numero : '))
numero3 = int(input('Informe um numero : '))

if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
  print('Sim, pelo menos dois dos números informados são iguais.')

else:
  print('Não, todos os números informados são diferentes.')