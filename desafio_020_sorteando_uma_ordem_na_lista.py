'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
b = str(input('1º aluno '))
c = str(input('2º aluno '))
d = str(input('3º aluno '))
e = str(input('4º aluno '))

lista = [b, c, d, e]

shuffle(lista) #embaralhar

print('A ordem de apresentação será')

print(lista)
