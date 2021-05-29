"""
Exercício Python 11:
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
l = float(input('Qual a medida da lagura da parede '))
a = float(input('Qual a medida da Altura da parede '))
p = l*a
# cada litro de tinta cobre 2m2
t = p/2
print('A quantidade de tinta nessesaria é', t, 'l')
