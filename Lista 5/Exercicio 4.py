## Exercicio 4 lista 5   Dobrar lista 
def dobrar_lista():
  lista = [20,40,50,60,70,89]
  lista_dobrada = []
  for i in lista: ## percorre a lista original
    lista_dobrada.append(i * 2) ## percorre toda a lista ja multiplicando todos os numeros que estao dentro da lista, e ja adiciona ela a lista dobrada
  print(lista_dobrada) ## imprime a lista
  return lista_dobrada ##  retorna a lista


chamar = dobrar_lista() ## chama a função