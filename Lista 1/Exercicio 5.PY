#### Exercicio 5 lista 1
## Calcule a média de 3 notas e verifique se é igual a 7.0.

nota1 = float(input('Informe sua nota'))
nota2 = float(input('Informe sua nota'))
nota3 = float(input('Informe sua nota'))

media = (nota1 + nota2 + nota3) / 3
maior = media > 7.0
print(f'A media do aluno foi de : {media:.2f} foi maior que : {maior}')