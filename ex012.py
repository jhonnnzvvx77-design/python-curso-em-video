#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input('qual é o preço do produto? '))

desconto = (preço * 5 / 100)
novo_preço = preço - desconto

print(f'o valor é {preço:.2f} o desconto é {desconto:.2f} e o resultado é {novo_preço:.2f}')
