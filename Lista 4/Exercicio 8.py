## Exercicio 8 lista 4

## Soma até negativo: Solicite números até que o usuário digite um número negativo. Mostre a soma dos números positivos digitados.


# 1. Começa a soma em zero
soma = 0

# 2. Loop infinito que só para com o 'break'
while True:
  numero = float(input("Digite um número (negativo para parar): "))

  # 3. Se o número for negativo, para o loop
  if numero < 0:
    break

  # 4. Se for positivo, adiciona à soma (ignora zeros)
  if numero > 0:
    soma += numero

# 5. Mostra o resultado final
print(f"A soma dos números positivos foi: {soma}")