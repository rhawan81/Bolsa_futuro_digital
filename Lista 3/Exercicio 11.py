## Exercicio 11 lista 3
## Peça um número e verifique se ele é múltiplo de 3 e de 4 ao mesmo tempo.
numero = int(input('Informe um numero:'))
if numero % 4 == 0 and numero % 3 == 1:
  print(f"Sim! O número {numero} atende às duas condições.")
  print(f"Ele é um múltiplo de 4 e deixa resto 1 ao ser dividido por 3.")
else:

  print(f"Não. O número {numero} não atende a uma ou ambas as condições.")