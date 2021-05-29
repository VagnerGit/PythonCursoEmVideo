"""
Exercício Python 12:
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Qual é preço sem desconto? R$'))
d = p*0.95
print('Preço sem desconto R${:.2f} com 5% de desconto R${:.2f}'.format(p, d))

