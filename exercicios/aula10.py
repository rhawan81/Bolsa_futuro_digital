# Solicita o primeiro número inteiro ao usuário
numero1 = int(input('Informe o primeiro numero: '))

# Solicita o segundo número inteiro ao usuário
numero2 = int(input('Informe o segundo numero: '))

# Realiza a divisão inteira (retorna apenas a parte inteira do quociente)
divisao_inteira = numero1 // numero2

# Calcula o resto da divisão
resto = numero1 % numero2

# Exibe a divisão inteira e o resto
print(f'Divisão inteira: {divisao_inteira}')
print(f'Resto da divisão: {resto}')
