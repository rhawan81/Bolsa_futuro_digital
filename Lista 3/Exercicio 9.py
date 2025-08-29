## Exercicio 9 lista 3
#Pergunte a quantidade de produtos no estoque e se é produto essencial (True/False).
##  Reponha se for essencial ou a quantidade for menor que 10.

# 1. Pergunta a quantidade de produtos e converte para número inteiro.
quantidade = int(input('Qual a quantidade do produto no estoque? '))

# 2. Pergunta se é essencial e converte a resposta (S/N) para um valor booleano (True/False).
#    Usar .upper() == 'S' é a forma segura de fazer isso.
resposta_essencial = input('O produto é essencial? (S/N): ')
eh_essencial = resposta_essencial.upper() == 'S'


# --- LÓGICA DE DECISÃO ---

# A condição verifica se a variável 'eh_essencial' é True OU se a 'quantidade' é menor que 10.
# Se qualquer uma das duas for verdadeira, o bloco do 'if' é executado.
if eh_essencial or quantidade < 10:
  print('\n---------------------------------')
  print('ATENÇÃO: Repor o estoque!')
  print('---------------------------------')
else:
  # Este bloco só é executado se AMBAS as condições forem falsas.
  # (Ou seja, o produto não é essencial E a quantidade é 10 ou mais).
  print('\nEstoque OK. Não é necessário repor no momento.')