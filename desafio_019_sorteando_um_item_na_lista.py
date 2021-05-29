"""
Exercício Python 19:
    Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e
escrevendo na tela o nome do escolhido.
"""

from random import choice
b = str(input('1º aluno '))
c = str(input('2º aluno '))
d = str(input('3º aluno '))
e = str(input('4º aluno '))

lista = [b, c, d, e]

escolhido = choice(lista)

print('O escolhido foi você ', escolhido)
