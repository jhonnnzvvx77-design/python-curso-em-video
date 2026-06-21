#Faça um programa que leia a largura e a altura de uma parede, calcule sua área e mostre quantos litros de tinta serão necessários, sabendo que cada litro pinta 2m².

largura = float(input('qual é a largura ?' ))
altura = float(input ('qual é a altura ?' ))

area = largura * altura
tinta = area / 2

print(f'a largura é {largura} a altura é {altura} e a area é {area} ')
print(f' Você precisará de {tinta:.2f} Litros de tinta ')