### Exercicio 4 lista 1

### Peça dois números ao usuário, calcule a soma e verifique se é maior que 20.

num1 = int(input('Informe um Numero:'))
num2 = int(input('Informe um Numero:'))

soma = num1 + num2
maior = soma > 20 ## verifica se a soma e maior que 20

print(f'A soma dos numeros é de {soma} é maior que : {maior}' ) ## imprime a soma dos numeros e retorna um valor booleano