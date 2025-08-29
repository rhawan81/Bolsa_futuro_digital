## Exercicio 10 lista 3
##  Solicite a altura e o peso,
## e verifique se o IMC está fora da faixa saudável (18.5 a 24.9).

altura = int(input('Informe sua altura:'))
peso = float(input('Informe seu peso:'))

imc = peso / altura
if imc >= 18.5 :
  print('saudavel')
elif imc < 25:
  print('Classificação Peso Normal')
else:
  print('Classificação: Acima do peso (Sobrepeso ou Obesidade)')