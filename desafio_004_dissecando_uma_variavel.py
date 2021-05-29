"""
Exercício Python 4:
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
"""

algo = input('Digite algo: ')
print(type(algo))
print('Só tem espaço ', algo.isspace())
print(f'O {algo} é alfabetico? ', algo.isalpha())
print(f'O {algo} é alfabetico e numerico? ', algo.isalnum())
print(f'O {algo} é Nº? ', algo.isnumeric())
print(f'O {algo} é decimal? ', algo.isdecimal())
print(f'O {algo} esta tudo em letra maiuscula? ', algo.isupper())
print(f'O {algo} esta tudo em letra minuscula? ', algo.islower())
print(f'O {algo} a 1º letra é maiuscula? ', algo.istitle())
