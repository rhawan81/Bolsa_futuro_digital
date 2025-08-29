## Exercicio 3 lista 3
### Pergunte a nota de um aluno e se ele fez trabalho extra (True/False).
##  Aprove se a nota for ≥ 7 ou se fez trabalho extra.
nota = float(input('Informe sua nota:'))
resposta_trabalho = input('Fez o trabalho extra? (S/N): ')
fez_trabalho = resposta_trabalho.upper() == 'S' ## captura a resposta do trabalho
if nota >= 7 or fez_trabalho: ## operador logico quando um for falso o outro sera verdadeiro
  print('Aprovado !')

else:
  print('VOCE DEIXOU DE REALIZAR ALGUMA ATIVIDADE')