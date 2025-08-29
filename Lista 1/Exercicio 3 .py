## Exercicio 3 Lista 01
## Peça dois números ao usuário e mostre qual é o maior ou se são iguais.

number = int(input('Informe um numero:'))
number2 = int(input('Informe outro Numero:'))

maior =  (number *(number > number2)) + (number2 * ( number2 > number)) ## metodo para verificar qual numero é maior sem utilizar if e else:

print(f'O maior numero digitado é {maior}') # imprime o valor maior