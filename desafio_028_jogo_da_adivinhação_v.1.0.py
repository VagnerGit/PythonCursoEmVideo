'''Exercício Python 28:
 Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
print('-='*30)
print('\033[1:34:46mVou pensar em um Nº de 0 a 5. Tente adivinhar...\033[m')
print('-='*30)
pc = randint(0, 5)
usuario = int(input('Adivinha o Nº que pensei: '))
if pc == usuario:
    print(f'Parabens escolhi {pc} e você acertou {usuario}')
else:
    print(f'Eu escolhi {pc} e você {usuario}. Não desista ')
