## Exercicio 12 lista 3
##   Solicite a idade e se possui autorização dos pais (True/False).
## Permita a entrada se for maior de idade ou tiver autorização.

idade = int(input('Informe sua idade:'))
autorização = input('Voce tem Autorização ') .upper()
if idade >= 18 and autorização == 'S':
  print('Entrada Permitida com Sucesso !')
else:
  print('Entrada Negada. É necessário ser maior de idade ou ter autorização dos pais.')