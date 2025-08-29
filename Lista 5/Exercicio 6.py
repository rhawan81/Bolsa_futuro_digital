## Exercicio 6 lista 5
### Crie uma função media(*notas) que receba várias notas (usando parâmetros variáveis) e retorne a média.
def media():
  lista_de_notas = [] ## lista vazia
  for i in range(3): ## pede ao usuario 3 notas
    nota = float(input('Informe sua nota:'))
    lista_de_notas.append(nota) ## armazena as notas dentro da lista
  media = sum(lista_de_notas) / 3 ## realiza a operação de soma e divide por 3
  return media # retorna a media


chamar = media()
print(f'Sua media é de {chamar:.2f}') ## mopstra a media do aluno