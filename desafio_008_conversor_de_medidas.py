'''Exercício Python 8: Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros.'''

n = float(input('Digite uma distancia em metros '))
#cen = n*100
#mil = n*1000
print('Metro {};\n centimetro {};\n milimetro {}.'.format(n, (n*100), (n*1000)))
