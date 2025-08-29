<<<<<<<< HEAD:Lista 2/Exercicio 9.py
## Exercicio 9 lista 2

## Peça dois números e mostre se o primeiro é menor que o segundo.
numero = int(input('Informe um Numero:'))
numero2 = int(input('Informe outro'))
menor  = (numero * (numero < numero2)) + (numero2 * (numero2 <= numero))
========
numero = int(input('Informe um Numero:'))
numero2 = int(input('Informe outro'))
menor  = (numero * (numero < numero2)) + (numero2 * (numero2 <= numero))
>>>>>>>> a48e065759d3e5e8fab80f827dc0c76376378931:exercicios/numeromenor.py
print(menor)