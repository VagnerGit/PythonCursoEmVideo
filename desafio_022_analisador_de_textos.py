'''Exercício Python 22:
 Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite nome completo: ')).strip()
print('-='*30)
print(f'Todas letras MAISCULAS {nome.upper()}')
print('-='*30)
print(f'Todas as letras munúsculas {nome.lower()}')
print('-='*30)
print(f'Existem {len(nome) - nome.count(" ")} letras no nome todo')
print('-='*30)
print(f'O primeiro nome tem {len(nome.split()[0])} letras')
print('-='*30)
print(f'O primeiro nome tem {nome.find(" ")} letras [c/ find] ')
        #O 1º espaço aparece no fianal do 1º nome
print('-='*30)
