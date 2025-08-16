number = int(input('Informe um numero:'))
number2 = int(input('Informe outro Numero:'))
maior = (number * (number > number2)) + (number2 * (number2 >= number)) # no primeiro parentese ele verifica se o numero e maior que o numero 2 se for verdadeiro ele ira retornar 1 se for falso retornara 0 ou seja caso o digitado seja 10  e 7 , o 10 ira multiplicar por 1.

### ja no segundo caso ele ira verificar a mesma coisa  so que com um porem agora foi adicionado o >= pq caso o numero seja igual ele ira retornar um valor booleano
iguais = (number == number2) # -> comparação ou seja esta verificando se eles sao iguais
print(f'O maior número é: {maior}') # -> imprime o numero maior
print(f'Os numeros sao iguais :{iguais}') #-> imprime que os numeros sao iguais