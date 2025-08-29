## Exercicio 8 lista 3
## Peça o salário e verifique se ele está entre 2000 e 5000 ou é exatamente 10000.

salario = float(input('Informe seu salario:'))
if salario >= 2000 and salario <= 5000 or salario == 10000:
  print(f'O salário de R$ {salario:.2f} atende aos critérios especificados.')

else:
  print(f'O salário de R$ {salario:.2f} não está na faixa de 2000-5000 nem é igual a 10000.')