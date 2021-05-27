'''Exercício Python 5:
 Faça um programa que leia um número Inteiro e
mostre na tela o seu sucessor e seu antecessor.'''

n = int(input('digite um numero inteiro '))
#ant = n-1
#post = n+1
#print('O antecessor de {} é {} e posterior é {}' .format(n, ant, post))
print('{} o antercessor é {} o sucessor é {}'.format(n, (n-1), (n+1)))
