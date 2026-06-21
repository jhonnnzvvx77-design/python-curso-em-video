#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('quanto dinheiro você tem na carteira? ' ))
cotação = 3.27
dolares = reais / cotação
print(f'{reais} convertido para dolares é {dolares:.2f} ')