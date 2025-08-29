## Exercicio 8 lista 2

## Peça dois números e mostre se o primeiro é maior que o segundo.

num1 = int(input('Informe um numero : '))
num2 = int(input('Informe um numero:'))

maior = (num1 * (num1 > num2)) + (num2 * (num2 > num1))
print(f'O numero maior é o {maior}')
