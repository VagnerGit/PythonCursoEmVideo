'''Exercício Python 46:
Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
1 segundo entre eles.'''

from emoji import emojize
from time import sleep
print('\033[31mContagem regressiva\033[m')
n = int(input('Digite Nº para contagem: '))
for c in range(n, -1, -1):
    sleep(1)
    print(c)
print(emojize('\033[31mLANÇAMENTO\033[m  :rocket:'))
