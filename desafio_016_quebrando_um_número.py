"""
Exercício Python 16:
Crie um programa que leia um
número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

'''import math
n = float(input('Digite Nº com casas decimais = '))
print(math.floor(n), math.ceil(n), round(n)) # ceil arredonda p/ cima, floor para baixo e round arredonda'''

from math import trunc
num = float(input('Digite um Nº com virgula: '))
print('O valor de {} e sua parte inteira é {}'.format(num, trunc(num)))# int(num) ou trunc
