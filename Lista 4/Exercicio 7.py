## Exercicio 7 lista 4

## Contar positivos e negativos: Peça 6 números e conte quantos são positivos, negativos ou zero.


# 1. Inicializa os contadores
positivos = 0
negativos = 0
zeros = 0

# 2. Loop que repete 6 vezes
for i in range(6):
  # Pede um número ao usuário
  numero = float(input("Digite um número: "))

  # 3. Classifica e conta o número
  if numero > 0:
    positivos += 1
  elif numero < 0:
    negativos += 1
  else:
    zeros += 1

# 4. Mostra o resultado final
print("\n--- Resultado da Contagem ---")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")