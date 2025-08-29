## Exercicio 9 lista 4
## gere um numero aleatorio de 1 a 20 e peça o usuario para advinhar, usando while ate acertar

from random import randint

escolha_aleatoria = randint(1,20)
tentativas = 0
while True:
  escolha_user =int(input('Informe seu numero:'))
  tentativas += 1

  if escolha_user == escolha_aleatoria:
    print(f'Parabens Voce Acertou meu Numero com {tentativas} tentativas')
    break

  elif escolha_user > escolha_aleatoria:
    print('Numero Menor , tente novamente')

  else:
    print('Numero maior, Tente novamente')