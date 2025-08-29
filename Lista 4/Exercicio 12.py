## Exercicio 12 lista 4
## Primos até N: Peça um número N e mostre todos os números primos até ele.

# --- Programa para Encontrar Números Primos até N ---

# 1. Peça ao usuário um número e o converta para inteiro.
limite_n = int(input("Digite um número inteiro maior que 1: "))

# Validação para garantir que o número é pelo menos 2
if limite_n < 2:
    print("Por favor, informe um número maior que 1.")
else:
    print(f"\n--- Números primos até {limite_n} ---")

    # 2. O primeiro loop (externo) vai de 2 até o número que o usuário digitou.
    #    A variável 'numero_para_testar' será 2, depois 3, depois 4, e assim por diante.
    for numero_para_testar in range(2, limite_n + 1):

        # 3. Assumimos que o número é primo até que se prove o contrário.
        #    Esta variável 'eh_primo' reinicia como 'True' para cada novo número.
        eh_primo = True

        # 4. O segundo loop (interno) tenta encontrar um divisor.
        #    Ele vai de 2 até um número antes do que estamos testando.
        for divisor in range(2, numero_para_testar):

            # 5. Se a divisão for exata (resto igual a 0)...
            if numero_para_testar % divisor == 0:
                # ...então o número NÃO é primo.
                eh_primo = False
                # Como já provamos que não é primo, podemos parar de testar este número.
                break

        # 6. Depois que o loop interno termina, verificamos a variável.
        #    Se 'eh_primo' continuou 'True', significa que nenhum divisor foi encontrado.
        if eh_primo:
            # Então, o número é primo e nós o imprimimos!
            print(numero_para_testar)