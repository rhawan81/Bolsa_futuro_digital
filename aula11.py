# Solicita que o usuário informe um número inteiro
numero = int(input('Informe um numero: '))

# Calcula o quadrado do número (o número elevado à potência de 2)
quadrado = numero ** 2

# Calcula o número elevado à potência de si mesmo
# Ex: se numero for 2, sera 2 elevado a 2 (4)
# Ex: se numero for 3, sera 3 elevado a 3 (27)
raiz_quadrada = numero ** numero # Nota: O nome da variavel 'raiz_quadrada' pode ser confuso aqui,
                                 # pois a operacao e uma potencia, nao uma raiz quadrada.

# Exibe o resultado da potencia (numero elevado a si mesmo)
print(f'O numero ao quadrado é: {quadrado}')
print(f'O numero {numero} elevado a {numero} é: {raiz_quadrada}')
