## Exercicio 6 lista 3
##  Peça a idade e se tem carteira de motorista (True/False).
## Permita dirigir se idade ≥ 18 e tiver carteira.

idade = int(input('Informe sua idade :'))
carteira = input('TEM CARTEIRA ?') .upper()

if idade >= 18 and carteira == 'S':
  print('Voce esta permitido dirigir')
elif idade < 18 and carteira != 'S':
  print('Você não pode dirigir, pois é menor de idade e não tem carteira.')
elif idade < 18:
  print('Voce nao pode dirigir , pois e menor de idade')

else:
    print('Você não atende a todos os requisitos necessários para dirigir.')