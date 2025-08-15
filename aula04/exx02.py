## sistema de notas --------
#_---------------------
nome = input('Informe seu nome:')
nota = float(input('Informe uma nota:'))
if nota >= 7:
    print(f'O aluno {nome} foi aprovado com a nota de {nota}')
elif nota > 5 and nota < 7 :
    print(f'O aluno {nome} esta em recuperação com a nota de {nota}')
else:
    print(f'O aluno {nome} esta Reprovado !')        