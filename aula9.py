salario = float(input('Informe seu salario :'))
# Calcula o valor do aumento de 15%
# 15% de um valor é o mesmo que multiplicar por 0.15
valor_do_aumento = salario * 0.15

# Calcula o novo salário somando o salário original com o valor do aumento
novo_salario = salario + valor_do_aumento
# Exibe o valor do novo salário calculado
print(f'O salário original é: R$ {salario:.2f}')
print(f'O valor do aumento (15%) é: R$ {valor_do_aumento:.2f}')
print(f'O novo salário com aumento de 15% é: R$ {novo_salario:.2f}')
