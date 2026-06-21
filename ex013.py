#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? '))

aumento = (salario * 15 / 100)
novo_salario = salario + aumento

print(f'o salário é {salario:.2f} com os 0.15 de aumento fica {novo_salario:.2f} ')
