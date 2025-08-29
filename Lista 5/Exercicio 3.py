## Exercicio 3 lista 5
def par_impar():
  numero = int(input('Informe um numero:'))
  if numero % 2 == 0:
    return 'Par'
  else:
    return 'Impar'


chamar = par_impar()
print(chamar)