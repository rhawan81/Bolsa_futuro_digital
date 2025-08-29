## Exercicio 5 lista 5
## Explique, em código, a diferença entre uma variável global e uma variável local.

def explicar():
  nome = input('Informe seu nome: ') ## variavel local ou seja so existe dentro da função caso queira chamar ela fora da função ira da erro


chamar = explicar() ## variavel global que esta fora da função 
print(explicar())