#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

M = int(input('Digite um valor em metros: '))
cm = M * 100
mm = M * 1000
print(f'{M} equivalem a {cm} centímetros e {mm} milímetros ')
