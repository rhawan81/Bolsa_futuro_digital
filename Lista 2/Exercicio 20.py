## Exercicio 20 lista 2
## Peça dois números e mostre o menor valor (sem if).

numero = int(input('Informe um Numero:'))
numero2 = int(input('Informe outro'))
menor  = (numero * (numero < numero2)) + (numero2 * (numero2 < numero))
print(f'O menor valor foi {menor}')
