## Exercicio 7 lista 5
###  Escreva uma função calculadora(a, b, operacao) que receba dois números e uma operação
# ("+", "-", "*", "/") e retorne o resultado.
def calculadora():
  a = int(input('Informe um numero:'))
  b = int(input('Informe um numero:'))
  operacao = input('(+), (-),(*)')
  if operacao == '+':
    return a + b
  elif operacao == '-':
    return a - b
  elif operacao == '*':
    return a * b

calcular = calculadora()
print(calcular)