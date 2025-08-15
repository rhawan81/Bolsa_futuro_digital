idade = int(input('informe sua idade:'))
print("""1.VIP
      (SIM)
      (NAO)""")
escolha = int(input('(1/2)'))
if escolha == 1 and idade > 18:
    print('Entrada permitida')
elif escolha == 2 and idade < 18:
    print('VOCE E MENOR DE IDADE ')
else:
    print('voce nao atende aos requisitos')        