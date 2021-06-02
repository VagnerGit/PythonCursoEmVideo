'''Exercício Python 30:
Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input('\033[32m Digite um número inteiro '))
if n % 2 == 0:
    print('O número é', n, ' é par')
else:
    print("O núnmero é ", n, " impar")

