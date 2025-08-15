name = input('Informe seu nome:')
valor_compra = float(input('Informe o valor da sua compra:'))
escolha = int(input( """""1.COMUM
               2.VIP
               3.PREMIUM"""))
               
if escolha == 3:
    desconto = valor_compra - (valor_compra * 0.2) 
    print(f'O valor desconto foi de {desconto}')
    
elif escolha == 2: 
    desconto_vip = valor_compra - (valor_compra * 0.1) 
    print(f'O valor do seu desconto foi de {desconto_vip}')
    
else:
    print('VOCE NAO RECEBEU NENHUM DESCONTO')    
                  