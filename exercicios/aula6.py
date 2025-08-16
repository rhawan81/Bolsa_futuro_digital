# Solicita que o usuário digite um número inteiro
numero = int(input('Informe um número inteiro: '))

# Calcula o resto da divisão do número por 3
# O operador '%' (módulo) retorna o resto da divisão
resto = numero % 3

# Define variáveis booleanas com base na condição
# 'True' é tratado como 1, 'False' como 0 em operações aritméticas
e_igual_a_um = (resto == 1)
nao_e_igual_a_um = (resto != 1)

# Imprime a mensagem correspondente multiplicando a string pelo booleano
# Se o booleano for True, a string é impressa uma vez. Se for False, não é impressa.
print(f'O resto da divisão de {numero} por 3 é igual a 1.' * e_igual_a_um, end='')
print(f'O resto da divisão de {numero} por 3 não é igual a 1. O resto é {resto}.' * nao_e_igual_a_um, end='')
